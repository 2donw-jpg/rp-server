from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Profile
from .serializer import ProfileSerializer


@api_view(['GET'])
def getData(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def addProfile(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)