from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from connect_app.models import Message, HouseListing

from members.models import Member
from members.serializers import HouseListingSerializer, MessageSerializer, UserProfileSerializer, HomeListingImageSerializer


@api_view(['GET'])
def matchedMembersList(request):
    location = request.GET.get('location') or None
    age = request.GET.get('age') or None
    gender = request.GET.get('gender') or None
    education = request.GET.get('education_level') or None

    
    member_list = Member.objects.all() # query all members for now
    if location:
        member_list = member_list.filter(preferred_location__icontains=location)
    if age:
        member_list = member_list.filter(age=age)   
    if gender:
        member_list = member_list.filter(gender__iexact=gender)
    if education:
        member_list = member_list.filter(education_level__icontains=education)
 

    serializer = UserProfileSerializer(member_list, many=True)
    return Response(serializer.data, status=200)


    

@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def upload(request):
    if request.method == 'GET':
        all_listings = HouseListing.objects.all()
        serializer = HouseListingSerializer(all_listings, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = request.POST.copy()
        photo_upload = request.FILES
        serializer = HouseListingSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            if photo_upload:
                for image in photo_upload:
                    image_data = { "house_listing": instance.id, 'upload': photo_upload[image]}
                    image_serializer = HomeListingImageSerializer(data=image_data)
                    if image_serializer.is_valid():
                        image_serializer.save()
                    else:
                        instance.delete()
                        return JsonResponse(image_serializer.errors, status=400)

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


     
