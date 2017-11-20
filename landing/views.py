from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from .forms import ContactForm, SignUpForm
from blog.models import Post
# Create your views here.
def home(request):
	# title = 'Welcome'
	# if request.user.is_authenticated():
	# 	title = 'My title %s' %(request.user)
	# form = SignUpForm(request.POST or None)
	# if form.is_valid():
	# 	instance = form.save(commit = False)
	# 	full_name = form.cleaned_data.get('full_name')
	# 	if not full_name:
	# 		full_name = 'sapphire'
	# 	instance.full_name = full_name
	# 	instance.save()
	form = ContactForm(request.POST or None)
	gambling_latest = Post.objects.filter(classify = 1).order_by('-publish')[:1].get()
	affiliate_latest = Post.objects.filter(classify = 2).order_by('-publish')[:1].get()
	forex_latest = Post.objects.filter(classify = 3).order_by('-publish')[:1].get()
	context = {
		'form' : form,
		'gambling_latest' : gambling_latest,
		'affiliate_latest' : affiliate_latest,
		'forex_latest' : forex_latest,
	}
	if form.is_valid():
		form_email = form.cleaned_data.get('email')
		form_full_name = form.cleaned_data.get('full_name')
		form_message = form.cleaned_data.get('message')
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "%s: %s via %s" %(form_full_name, form_message, form_email)
		# html_message = """
		# 	<h1>Hello, This is html message</h1>
		# """
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email,
				# html_message = html_message,
				fail_silently = False)
	if request.is_ajax():
		count = int(request.POST.get('val'))
		gambling_latest = serializers.serialize('json', Post.objects.filter(classify = 1).order_by('-publish')[count - 1 : count])
		affiliate_latest = serializers.serialize('json', Post.objects.filter(classify = 2).order_by('-publish')[count - 1 : count])
		forex_latest = serializers.serialize('json', Post.objects.filter(classify = 3).order_by('-publish')[count - 1 : count])
		latest_posts = {
				'gambling_latest' : gambling_latest,
				'affiliate_latest' : affiliate_latest,
				'forex_latest' : forex_latest,
			}
		return JsonResponse({'status' : True, 'latest_posts' : latest_posts})
	return render(request, 'landing/home.html', context)