from django.shortcuts import redirect
from .models import Person, Slider, Service, Portfolio
from django.views.generic import ListView, TemplateView
from bootstrap_modal_forms.generic import BSModalReadView
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages

#Slider
class SliderList(ListView):
	model = Slider
	context_object_name = 'sliders'
	template_name = 'home.html'

#Service
class ServiceList(ListView):
	model = Service
	context_object_name = 'services'
	template_name = 'service.html'
	paginate_by = 8

#Portfolio
class FolioList(ListView):
	model = Portfolio
	context_object_name = 'portfolios'
	template_name = 'portfolio.html'
	paginate_by = 4

#Detail Portfolio
class FolioReadView(BSModalReadView):
	model = Portfolio
	template_name = 'read_folio.html'

class ContactView(TemplateView):
	template_name = 'contact.html'

def send(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']

		template = render_to_string('email.html', {'name' : name, 'email' : email, 'message' : message})

		email = EmailMessage(subject, template, email, ['ddam.java@gmail.com'])
		
		email.fail_silently = False
		email.send()

		return redirect('contact')