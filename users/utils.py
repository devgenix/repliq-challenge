# Native imports
import os

# Third Party Imports
from rest_api_payload import success_response, error_response

def SuccessResponse(message, serializer=None):
    if serializer is not None:
        assert serializer.data is not None, "Serializer has no data"
    
    if serializer == None:
        payload = success_response(
            status="Success",
            message=message,
            data=""
        )
        
        return payload
    
    else:
        payload = success_response(
            status="Success",
            message=message,
            data=serializer.data
        )
        
        return payload

def ErrorResponse(message):

    payload = error_response(
        status="Error",
        message=message,
    )
    
    return payload

def validate_sharing_id(sharing_id):
    # Remove the leading "?" if it's present
    if sharing_id.startswith("?"):
        sharing_id = sharing_id[1:]
    
    # Check if the sharing ID is in the correct format
    if sharing_id.startswith("wt.mc_id="):
        return True
    else:
        return False
