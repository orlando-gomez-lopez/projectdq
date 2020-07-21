from .models import Search
from rest_framework import generics
from .serializers import SearchSerializer

class SearchAPIView(generics.ListCreateAPIView): 
    ''' generic api view countries model '''
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
