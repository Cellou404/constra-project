from django.shortcuts import render
from faq.models import FAQ

# Create your views here.

def faq(request):
    faq_first = FAQ.objects.filter(subject="CONSTRUCTION", is_active=True).order_by('-date_created')
    faq_second = FAQ.objects.filter(subject="SAFETY", is_active=True).order_by('-date_created')

    context = {
        'faq_first': faq_first,
        'faq_second': faq_second,
    }

    return render(request, 'faq/faq.html', context)
