from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def aboutus(request):
    return render(request, 'about-us.html', {})

def rooms(request):
    return render(request, 'rooms.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})

def services(request):
    return render(request, 'services.html', {})

def blog(request):
    return render(request, 'blog.html', {})