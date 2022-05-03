from django.shortcuts import render
from django.views import generic
# from django.contrib.auth.decorators import login_required

from members.models import Member


from .filters import MemberFilter

def HomeView(request):
    return render(request, 'general/home.html', {})

# @login_required
def MatchedMembersList(request):
    # member_list = MemberFilter(request.GET, queryset=Member.objects.all()) # query all members for now
    member_list = Member.objects.all() # query all members for now
    return render(request, 'connect_app/connects_list.html', 
    { 'member_list': member_list})