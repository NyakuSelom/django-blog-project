# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def do_login(request):
    if request.method == 'POST':
	uname = request.POST['username']
	passwd = request.POST['password']
	user = authenticate(username=uname,password=passwd)
        if user== None:
	    print "authentication failed"

	else:
	    if user.is_active:
		login(request, user)
	    else:
		print "Your Account Has been disabled"
	return Http
    
    form = LoginForm()
    return render_to_response('reg/do_login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated()
    })

@csrf_exempt
def do_logout(request):
    logout(request)
    return render_to_response('reg/do_logout.html')
