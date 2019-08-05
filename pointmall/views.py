from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET'])
def image_view(request, file_name):
    image_data = open('media/uploads/item_images/' + file_name, 'rb').read()
    return HttpResponse(image_data, content_type="image/JFIF")