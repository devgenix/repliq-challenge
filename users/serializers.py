
# Own imports
from django.contrib.auth import get_user_model
from users.utils import ErrorResponse

# Rest Framework Imports
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# Local Imports
from Assets.models import Company

User = get_user_model()

# Signup Serializer
class SignupSerializer(serializers.Serializer):

    def validate(self, *args):

        # Get the request data
        request = self.context.get('request')
        email = request.get('email')
        first_name = request.get('first_name')
        last_name = request.get('last_name')
        password = request.get("password")
        is_company_admin = request.get("is_company_admin", False)
        company = request.get("company", None)

        # Check if the data is valid
        if password is None:
            raise serializers.ValidationError(
                ErrorResponse("Password is required"))

        if first_name is None:
            raise serializers.ValidationError(
                ErrorResponse("First name is required"))

        if last_name is None:
            raise serializers.ValidationError(
                ErrorResponse("Last name is required"))

        if email is None:
            raise serializers.ValidationError(
                ErrorResponse("Email is required"))
        elif email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                ErrorResponse("Email already exists"))
            
        if is_company_admin not in ['True', 'False']:
            raise serializers.ValidationError(ErrorResponse("is_company_admin must be True or False"))
        else:
            if not company:
                raise serializers.ValidationError(
                    ErrorResponse("User is set as a Company admin, so Company is required"))
            else:
                company_object = Company.objects.filter(name=company).first()
                if not company_object:
                    raise serializers.ValidationError(
                        ErrorResponse(f"Company by name: {company} does not exist"))

        # Return the validated data
        return {"email": email, "first_name": first_name, 'last_name': last_name, 'password': password, 'is_company_admin': is_company_admin, 'company': company_object, 'request': request} 

    def save(self, **kwargs):

        # Get the validated data
        email = self.validated_data.get("email")
        password = self.validated_data.get("password")
        last_name = self.validated_data.get("last_name")
        first_name = self.validated_data.get("first_name")
        is_company_admin = self.validated_data.get("is_company_admin")
        company = self.validated_data.get("company")

        try:
            
            if is_company_admin == 'True':
                is_staff = True
            else:
                is_staff = False
            
            user = User.objects.create_user(
                email=email.lower(),
                first_name=first_name,
                last_name=last_name,
                password=password,
                is_company_admin=is_company_admin,
                is_staff=is_staff,
                company = company
            )

            serializer = UserSerializerWithToken(user, many=False)
            return serializer

        except Exception as e:

            raise serializers.ValidationError(ErrorResponse(e))

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    """
    It takes the user object,
    and then serializes it and returns it object
    """

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'is_company_admin',
        ]

    def to_representation(self, instance):
        # get the default representation dictionary from the parent class
        representation = super().to_representation(instance)

        # exclude any field(s) based on a condition
        if representation.get('is_staff') is False:
            representation.pop('is_staff', None)
        if representation.get('is_superuser') is False:
            representation.pop('is_superuser', None)
        if representation.get('is_company_admin') is False:
            representation.pop('is_company_admin', None)

        return representation

# Serializer for User token
class UserSerializerWithToken(UserSerializer):
    """
    It's a UserSerializer that also returns the access and refresh tokens for the user
    """
    access = serializers.SerializerMethodField(read_only=True)
    refresh = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        exclude = ['password', 'company', 'devices', 'date_joined', 'groups', 'user_permissions']

    # get access token
    def get_access(self, obj):
        token = RefreshToken.for_user(obj)

        token['id'] = obj.id
        token['is_active'] = obj.is_active
        token['first_name'] = obj.first_name
        token['last_name'] = obj.last_name
        token['email'] = obj.email
        token['is_company_admin'] = obj.is_company_admin
        token['is_staff'] = obj.is_staff
        return str(token.access_token)

    # get refresh token
    def get_refresh(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)
