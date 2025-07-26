from rest_framework import generics
from .models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminUser, IsOwnerUser

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'username': request.user.username,
            'email': request.user.email,
            'role': request.user.role
        })



class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        return Response({"message": f"Welcome Admin {request.user.username}!"})


class OwnerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerUser]

    def get(self, request):
        return Response({"message": f"Hello Owner {request.user.username}!"})
