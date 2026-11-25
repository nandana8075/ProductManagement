from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import ProductDb
from product.serializers import ProductSerializer, UserSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({
                "message":"User registered Successfully...!"
            })
        else:
            return Response(serializer_instance.errors)

class ProductListCreateView(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        qs=ProductDb.objects.all()
        serializer_instance=ProductSerializer(qs,many=True)
        return Response (serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=ProductSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({
                "messgae":"product details saved...! "
            })
        else:
            return Response(serializer_instance.errors)

class ProductUpdateRetrieveDeleteView(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        product_obj=get_object_or_404(ProductDb,id=pk)
        serializer_instance=ProductSerializer(product_obj)
        return Response(serializer_instance.data)

    def put(self,request,pk):
        product_obj=get_object_or_404(ProductDb,id=pk)
        form_data=request.data
        serializer_instance=ProductSerializer(product_obj,data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({
                "message":"detailes updated...!"
            })
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk):
        product_obj=get_object_or_404(ProductDb,id=pk)
        product_obj.delete()
        return Response({
            "message":"deleted successfully.....!"
        })
        
        
    
    
    
