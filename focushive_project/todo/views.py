from django.shortcuts import render

# Create your views here.

def home(request):

    client_list = [
        {
            'id' : 1,
            'name' : 'Zander Harding',
            'profession' : 'Software Engineer'
        },

        {
            'id' : 2,
            'name': 'John Smith',
            'profession' : 'Web developer'
        },

        {
            'id' : 3,
            'name': 'Luke Warren',
            'profession' : 'Systems Architect'
        }
    ]

    context = {'client': client_list}

    return render(request, 'index.html', context=context)

def register(request):
    return render(request, 'register.html')

def my_login(request):
    return render(request, 'my-login.html')

