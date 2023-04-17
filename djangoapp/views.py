from rest_framework.decorators import api_view
from models import User
from serializers import UserSerializer
from rest_framework.response import Response


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users)
    return Response(serializer.data)


@api_view(['GET'])
def getUserById(request, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user)
    return Response(serializer)


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateUser(request, id):
    user = User.object.get(id=id)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUser(request, id):
    user = User.object.get(id=id)
    user.delete()
    return Response('Deleted Successfully !')
