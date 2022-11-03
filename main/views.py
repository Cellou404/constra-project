from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User


# ==========Configuration for file upload with Tinymce Editor===============
import os
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from main.models import Service, Team, Testimonial
from projects.models import Project, ProjectCategory

# ==========Configuration for file upload with Tinymce Editor============= #
@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        file_obj = request.FILES['file']
        file_name_suffix = file_obj.name.split(".")[-1]
        if file_name_suffix not in ["jpg", "png", "gif", "jpeg", ]:
            return JsonResponse({"message": "Wrong file format"})

        upload_time = timezone.now()
        path = os.path.join(
            settings.MEDIA_ROOT,
            'tinymce',
            str(upload_time.year),
            str(upload_time.month),
            str(upload_time.day)
        )
        # If there is no such path, create
        if not os.path.exists(path):
            os.makedirs(path)

        file_path = os.path.join(path, file_obj.name)

        file_url = f'{settings.MEDIA_URL}tinymce/{upload_time.year}/{upload_time.month}/{upload_time.day}/{file_obj.name}'

        if os.path.exists(file_path):
            return JsonResponse({
                "message": "file already exist",
                'location': file_url
            })

        with open(file_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': file_url
        })
    return JsonResponse({'detail': "Wrong request"})
# ==========End Configuration for file upload with Tinymce Editor============= #

# =============================== HOME ====================================== #
def home(request):
    testimonials = Testimonial.objects.filter(is_active=True).order_by('-date_created')
    projects = Project.objects.filter(is_active=True).order_by('-date_created')[:6]
    p_categories = ProjectCategory.objects.filter(is_active=True)

    context = {
        'projects': projects,
        'p_categories': p_categories,
        'testimonials': testimonials,
    }
    return render(request, 'pages/home/home.html', context)

# =============================== ABOUT ====================================== #
def about(request):
    team = Team.objects.filter(is_active=True).order_by('date_created')

    context = {
        'team': team,
    }
    return render(request, 'pages/about.html', context)

# =============================== SERVICES ====================================== #
def services(request):
    services = Service.objects.filter(is_active=True).order_by('-date_created')
    return render(request, 'pages/services/services.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    services = Service.objects.filter(is_active=True).order_by('date_created')

    context = {
        'service': service,
        'services': services,
    }
    return render(request, 'pages/services/service-single.html', context)

# =============================== TEAM ====================================== #
def team(request):
    team = Team.objects.filter(is_active=True).order_by('date_created')
    return render(request, 'pages/team.html', {'team': team})

# =============================== TESTIMONIALS ====================================== #
def testimonials(request):
    testimonials = Testimonial.objects.filter(is_active=True).order_by('-date_created')
    return render(request, 'pages/testimonials.html', {'testimonials': testimonials})


# =============================== CONTACT ====================================== #
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        email_subject = f"You have a new message from CONSTRA"

        msgcxt = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message_template = 'pages/contact/email_sent.html'
        message_body = render_to_string(message_template, context=msgcxt)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        email_from = 'cskhamis94@gmail.com'
        recipient_list = [admin_email]

        s_message = EmailMessage(
            email_subject,
            message_body,
            email_from,
            recipient_list,
        )
        s_message.content_subtype = 'html'
        s_message.send()

        messages.success(request, "Thank you for contacting us. We will get back to you shortly")
        return redirect('contact')
    return render(request, 'pages/contact/contact.html')


# ========== 404 PAGE VIEW ================
def page_not_found_view(request, exception):
    return render(request, 'pages/404.html', {}, status=404)
