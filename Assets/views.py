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

# Own imports
from Assets.serializers import CompanyModelSerializer, CreateCompanySerializer
from Assets.models import Company

# Local imports
from users.utils import SuccessResponse, ErrorResponse

class CompanyView(APIView):
    """
    View to perform actions on the Company model.

    Functions:
        post: Create company
        get: Get Company information
        path: update company information
        delete: delete company information

    """
    permission_classes = [IsAuthenticated]
    
    # Create Company
    def post(self, request):
        serializer = CompanyModelSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(SuccessResponse("Created Company", serializer), status=201)
        else:
            return Response(serializer.errors, status=400)
    
    # Get company information
    def get(self, request, company_id):
        
        user = request.user
        if user.is_company_admin is not True or user.is_superuser is not True:
            return Response(ErrorResponse("You are not authorized to perform this action"))
        
        try:
            company = Company.objects.filter(id=company_id)
            
            serialized_data = CompanyModelSerializer(company, many=False)
            return Response(SuccessResponse("Retrieved Company", serialized_data))
        except Company.DoesNotExist: # return error if company was not found
            return Response(ErrorResponse(f"Company by id {company_id} doesn't exist"))
        except Exception as e: # return any other error
            return Response(ErrorResponse(e))
        
    # Update company information
    def patch(self, request, company_id):

        user = request.user
        provided_name = request.data.get('name')
        
        if user.is_company_admin is not True or user.is_superuser is not True:
            return Response(ErrorResponse("You are not authorized to perform this action"))
        
        if provided_name is None:
            return Response(ErrorResponse("Please provide name, only company name can be updated"))
        
        try:
            company = Company.objects.filter(id=company_id) # get company by id
            
            # updated company name
            company.name = provided_name
            company.save(updated_fields=['name'])
            
            # Return response
            return Response(SuccessResponse("Updated Company name"))
        
        except Company.DoesNotExist: # return error if company was not found
            return Response(ErrorResponse(f"Company by id {company_id} doesn't exist"))
        except Exception as e: # return any other error
            return Response(ErrorResponse(e))
        
    # Delete Company
    def delete(self, request, company_id):
        user = request.user
        if user.is_company_admin is not True or user.is_superuser is not True:
            return Response(ErrorResponse("You are not authorized to perform this action"))
        
        try:
            company = Company.objects.filter(id=company_id)
            
            company.delete()
            return Response(SuccessResponse(f"Deleted Comany by id: {company_id}"))
        except Company.DoesNotExist: # return error if company was not found
            return Response(ErrorResponse(f"Company by id {company_id} doesn't exist"))
        except Exception as e: # return any other error
            return Response(ErrorResponse(e))
        
class DeviceView(APIView):
    permission_classes = [IsAuthenticated]
    
    pass

class AllListView(APIView):
    permission_classes = [IsAuthenticated]
    
    pass

class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    pass