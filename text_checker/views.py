from rest_framework.decorators import api_view
from rest_framework.response import Response
from text_checker.serializers import TweetSerialzer
from text_checker.text_analysis import TextAnalyzer

text_analyzer = TextAnalyzer()

@api_view(['POST'])
def check_tweet(request):
    serializer = TweetSerialzer(data=request.data)
    if serializer.is_valid():
        text = serializer.validated_data['text']
        response = text_analyzer.analyze_text(text)
        return Response(response)
    else:
        return Response(serializer.errors, status=400)
