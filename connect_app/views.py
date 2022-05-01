from django.shortcuts import render

# Create your views here.
def connects_list(request):
    return render(request, 'connect_app/connects_list.html', {})