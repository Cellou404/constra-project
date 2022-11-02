from django.shortcuts import render, get_object_or_404

# ==========Configuration for file upload with Tinymce Editor===============
import os
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from main.models import Service, Team, Testimonial

# ==========Configuration for file upload with Tinymce Editor=============
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
# ==========End Configuration for file upload with Tinymce Editor=============

def home(request):
    testimonials = Testimonial.objects.filter(is_active=True).order_by('-date_created')

    context = {
        'testimonials': testimonials,
    }
    return render(request, 'pages/home/home.html', context)


def about(request):
    team = Team.objects.filter(is_active=True).order_by('date_created')

    context = {
        'team': team,
    }
    return render(request, 'pages/about.html', context)


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


def team(request):
    team = Team.objects.filter(is_active=True).order_by('date_created')
    return render(request, 'pages/team.html', {'team': team})


def testimonials(request):
    testimonials = Testimonial.objects.filter(is_active=True).order_by('-date_created')
    return render(request, 'pages/testimonials.html', {'testimonials': testimonials})


def contact(request):
    return render(request, 'pages/contact.html')


# ========== 404 PAGE VIEW ================
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
