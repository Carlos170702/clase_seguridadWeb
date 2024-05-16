from rest_framework.response import Response
from rest_framework import status as status_code


def success_response(message='Success', data=None, status=status_code.HTTP_200_OK):
    return Response({
        'status': True,
        'message': message,
        'data': data,
    }, status=status)


def error_response(message='Error', data=None, status=status_code.HTTP_500_INTERNAL_SERVER_ERROR):
    return Response({
        'status': False,
        'message': message,
        'data': data,
    }, status=status)
