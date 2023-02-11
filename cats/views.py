# from rest_framework import status
from rest_framework import viewsets
# from rest_framework import generics
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

from .models import Cat
from .serializers import CatSerializer


"""
@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'POST':
        serializer = CatSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)
"""


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'POST':
        return Response({"message": "Полученные данные", "data": request.data})
    return Response({"message": "Это был GET-запрос!"})


"""
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def cat_detail(request, id):
    cat = get_object_or_404(Cat, id=id)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = CatSerializer(cat)
    return Response(serializer.data, status=status.HTTP_200_OK)
"""


"""
class APICat(APIView):

    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


"""
class APICatDetail(APIView):

    def get(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cat = get_object_or_404(Cat, pk=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
class CatList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
"""


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
