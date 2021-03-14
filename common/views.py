from django.shortcuts import render
from django.shortcuts import redirect

from django.views import View

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
class login(View):
	management_grp_name = "management"
	trainer_grp_name = "trainer"

	def post(self, requests):
		username = requests.POST.get('username')
		password = requests.POST.get('password')

		user = authenticate(username=username, password=password)
		if user:
			user = User.objects.get(username=username)
			user_groups = user.groups.all()

			if user.groups.filter(name=self.management_grp_name).exists():
				return redirect('management/')
			elif user.groups.filter(name=self.trainer_grp_name).exists():
				return redirect('trainer/')
			else:
				context = {"error_message": "Internal Error. Please contact admin."}
				return render(requests, 'index.html', context=context)
		else:
			context = {"error_message": "Invalid username or password.Try again."}
			return render(requests, 'index.html', context=context)

	def get(self, requests):
		return render(requests, 'index.html')