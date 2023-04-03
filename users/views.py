# Own imports
from django.contrib.auth import get_user_model
User = get_user_model()
from users.serializers import UserSerializerWithToken, SignupSerializer

# Django imports
from django.db.models import Q
from django.contrib.auth import authenticate

# Rest Framework imports
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.parsers import FileUploadParser
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

# SimpleJWT imports
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend

# Third Party imports
from users.utils import SuccessResponse, ErrorResponse



####################################
###      Authentication          ###
####################################

### Signup View ###
class SignupView(APIView):
    
    def post(self, request):
        
        serializer = SignupSerializer(data=request.data, context={"request": request.data})
        if serializer.is_valid():
            user_serializer = serializer.save()
            
            return Response(SuccessResponse("Successfully Created User", user_serializer), status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### Login View ###
class MyTokenObtainPairView(TokenObtainPairView):
    """
    Custom Access token View
    """
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # get password and email from request data
        password = request.data.get("password", None)
        email = request.data.get("username", None)
        
        # check if email and password are provided
        if not password or not email:
            error_msg = "Provide email and password" if not email and not password else "Provide password" if not password else "Provide email" if not email else ""
            return Response(ErrorResponse(error_msg), status=status.HTTP_400_BAD_REQUEST)

        # check if a user exists with the email address provided
        user = User.objects.filter(Q(email__iexact=email.lower())).first()

        # raise an authentication failed error if a user with that email doesn't exist. 
        if user is None:
            raise exceptions.AuthenticationFailed(ErrorResponse("User does not exist!"))

        # check if password matches
        if user.check_password(password):
            # generate access and refresh token for the user
            serializer = UserSerializerWithToken(user)
            return Response(SuccessResponse("Login Successful",  serializer))

        # raise authentication failed error if it doesn't exist. 
        else:
            raise exceptions.AuthenticationFailed(ErrorResponse("Wrong password"))


### Refresh Token View ###
class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom Refresh token View
    """
    # serializer_class = CustomTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        try:
            # decode access token
            data = self.get_serializer().validate(request.data)
            decoded_payload = token_backend.decode(data['access'], verify=True)
            user_uid = decoded_payload['user_id']

            # get and serializer user
            user = User.objects.get(id=user_uid)
            serializer = UserSerializerWithToken(user)

            return Response({
                "status": "Success",
                "message": "Successfully refreshed token",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except TokenError as e:
            raise exceptions.AuthenticationFailed(ErrorResponse(str(e)))
