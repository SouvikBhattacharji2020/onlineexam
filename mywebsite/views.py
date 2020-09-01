from django.shortcuts import render		# just includde the html file

from django.http import HttpResponse  # just check request used.

#from mywebsite.froms import StudentForm

from mywebsite.models import login



# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
	return render(request, "index.html")	# use render(request, "file name.html ")

# def about(request):
# 	return render(request, "demo/base_file.html")

def test1(request):
	return render(request, "test1.html")

def about(request):
	
 	return render(request, "about.html")

# def splshscreen(request):
#  	return render(request, "SplshScreen.html")

def splshscreen(request):
 	return render(request, "splashscreen.html")

def loginpanel(request):
 	return render(request, "loginpanel.html")


def password_check(request,name):
    password1 = login.object.get(name=name)
    if password1.name=="Souvik" and password1.email=="souvik@gmail.com" and password1.password=="12345":
    	site="Proram.html"
    else:
    	site=""
    return render(request, site)
    