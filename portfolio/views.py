from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserEditForm, ProfileEditForm


@login_required
def portfolio(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance = request.user,
								data = request.POST)
		profile_form = ProfileEditForm(instance = request.user.profile,
										data = request.POST,
										files = request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated successfully !')
		else:
			messages.error(request, 'Error updating your profile...')
	else:
		user_form = UserEditForm(instance = request.user)
		profile_form = ProfileEditForm(instance = request.user.profile)
	return render(request, 'portfolio/portfolio.html', {'user_form' : user_form,
													'profile_form' : profile_form})