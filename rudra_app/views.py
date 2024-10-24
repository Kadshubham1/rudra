from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.utils import translation
from django.urls import reverse
from django.conf import settings

from .forms import AppointmentForm
from django.utils.translation import activate
import requests 


# Create your views here.

def change_language(request, language_code):
    # Check if the language is supported
    if language_code in [lang[0] for lang in settings.LANGUAGES]:
        # Store the language preference in the session
        request.session['django_language'] = language_code
        
        # Activate the new language
        translation.activate(language_code)
        
        # Get the previous page from the referer or go to home page
        next_url = request.META.get('HTTP_REFERER')
        if not next_url:
            next_url = '/'
            
        response = redirect(next_url)
        
        # Set the language cookie
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
        
        return response


# def send_whatsapp_message(phone_number, message):
#     # This is a placeholder function. You'll need to implement this
#     # using a WhatsApp Business API provider of your choice.
#     # Here's an example using a hypothetical API:
#     url = "https://api.whatsapp-provider.com/send"
#     payload = {
#         "phone": phone_number,
#         "message": message
#     }
#     headers = {
#         "Authorization": "Bearer YOUR_WHATSAPP_API_KEY"
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     return response.status_code == 200

def index(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            
            # Send email
            subject = 'New Appointment'
            message = f"""
            New appointment details:
            Name: {appointment.first_name}
            Email: {appointment.email}
            Phone: {appointment.phone}
            Gender: {appointment.gender}
            Date: {appointment.date}
            Department: {appointment.department}
            Comments: {appointment.comments}
            """
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
            
            # Send WhatsApp message to admin
            # admin_whatsapp = "YOUR_ADMIN_WHATSAPP_NUMBER"  # Replace with your WhatsApp number
            # send_whatsapp_message(admin_whatsapp, message)
            
            # Send default message to user on WhatsApp
            # user_message = f"Thank you for your appointment, {appointment.first_name}. We'll contact you soon to confirm."
            # send_whatsapp_message(appointment.phone, user_message)
            
            return JsonResponse({'success': True, 'message': 'Your appointment has been scheduled successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = AppointmentForm()
    
    context = {
        'form': form,
        # Add any other context data needed for your index page
    }
    return render(request, 'index.html', context)

def about(request):

    return render(request, 'about.html')

def services(request):

    return render(request, 'service.html')

def appointment(request):

    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            
            # Send email
            subject = 'New Appointment'
            message = f"""
            New appointment details:
            Name: {appointment.first_name}
            Email: {appointment.email}
            Phone: {appointment.phone}
            Gender: {appointment.gender}
            Date: {appointment.date}
            Department: {appointment.department}
            Comments: {appointment.comments}
            """
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
            
            # Send WhatsApp message to admin
            # admin_whatsapp = "YOUR_ADMIN_WHATSAPP_NUMBER"  # Replace with your WhatsApp number
            # send_whatsapp_message(admin_whatsapp, message)
            
            # Send default message to user on WhatsApp
            # user_message = f"Thank you for your appointment, {appointment.first_name}. We'll contact you soon to confirm."
            # send_whatsapp_message(appointment.phone, user_message)
            
            return JsonResponse({'success': True, 'message': 'Your appointment has been scheduled successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = AppointmentForm()
    
    context = {
        'form': form,
        # Add any other context data needed for your index page
    }
    return render(request, 'appointment.html', context)

def features(request):

    return render(request, 'feature.html')

def blog(request):

    return render(request, 'blog.html')

def team(request):

    return render(request, 'team.html')

def testmonial(request):

    return render(request, 'testimonial.html')

def contact(request):

    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            
            # Send email
            subject = 'New Appointment'
            message = f"""
            New appointment details:
            Name: {appointment.first_name}
            Email: {appointment.email}
            Phone: {appointment.phone}
            Gender: {appointment.gender}
            Date: {appointment.date}
            Department: {appointment.department}
            Comments: {appointment.comments}
            """
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
            
            # Send WhatsApp message to admin
            # admin_whatsapp = "YOUR_ADMIN_WHATSAPP_NUMBER"  # Replace with your WhatsApp number
            # send_whatsapp_message(admin_whatsapp, message)
            
            # Send default message to user on WhatsApp
            # user_message = f"Thank you for your appointment, {appointment.first_name}. We'll contact you soon to confirm."
            # send_whatsapp_message(appointment.phone, user_message)
            
            return JsonResponse({'success': True, 'message': 'Your appointment has been scheduled successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = AppointmentForm()
    
    context = {
        'form': form,
        # Add any other context data needed for your index page
    }
    return render(request, 'contact.html', context)

def get_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Your appointment has been scheduled successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = AppointmentForm()
    
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)