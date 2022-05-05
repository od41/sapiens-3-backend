from rest_framework.decorators import api_view
from rest_framework.response import Response

from members.models import Member
from members.serializers import UserProfileSerializer


@api_view(['GET'])
def matchedMembersList(request):
    location = request.GET.get('location') or None
    age = request.GET.get('age') or None
    gender = request.GET.get('gender') or None

    
    member_list = Member.objects.all() # query all members for now
    if location:
        member_list = member_list.filter(preferred_location__icontains=location)
    if age:
        member_list = member_list.filter(age=age)   
    if gender:
        member_list = member_list.filter(gender__iexact=gender)

    serializer = UserProfileSerializer(member_list, many=True)
    return Response(serializer.data, status=200)