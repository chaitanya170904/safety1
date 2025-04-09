import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
from .image_analysis import ImageAnalyzer 


logger = logging.getLogger(__name__)

class ImageAnalyzerAPI(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.analyzer = ImageAnalyzer()  

    def post(self, request):
        try:
            image_file = request.FILES.get('image')
            if not image_file:
                return Response(
                    {'error': 'No image file provided'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            temp_path = 'temp_image.jpg'
            with open(temp_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)
            analysis_result = self.analyzer.analyze_image(temp_path)
            os.remove(temp_path)
            return Response({'analysis_result': analysis_result}, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error processing image: {str(e)}")
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )