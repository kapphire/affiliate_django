from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'full_name', 'timestamp']
	form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)