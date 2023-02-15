from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from urllib.parse import unquote
from .utils.word_finder import WordFinder

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class SearchCoordsView(View):
    def get(self, request):
        product_name = unquote(request.GET.get('product', ''))
        products = Product.objects.all()
        product_names = [product.name for product in products]
        finder = WordFinder(product_names)
        longest_name = finder.longest_word(product_name)
        if longest_name == '':
            return HttpResponseBadRequest('No product was found that can be formed with the letters provided.')
        
        longest_product = Product.objects.get(name=longest_name)
        response_data = {
            'id': longest_product.id,
            'reference': longest_product.reference,
            'name': longest_product.name,
            'volume': longest_product.volume,
            'created': longest_product.created
        }
        return JsonResponse(response_data)