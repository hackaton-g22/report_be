from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from hackcodev.models.desaparecidos import Desaparecido
from hackcodev.serializers.desaparecidoSerializer import DesaparecidoSerializer


class DesaparecidosCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Desaparecido.objects.all()
    serializer_class = DesaparecidoSerializer
    
    def post(self,request,*args,**kwargs):
        serializer = DesaparecidoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status= status.HTTP_201_CREATED)


class DesaparecidosDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Desaparecido.objects.all()
    serializer_class = DesaparecidoSerializer

    def get(self, request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self, request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self, request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class DesaparecidosListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Desaparecido.objects.all()
    serializer_class = DesaparecidoSerializer

    def get(self, request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
