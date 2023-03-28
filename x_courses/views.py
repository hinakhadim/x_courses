from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_courses(request):
    return Response({'message': 'X Courses 1 is working'})
