from rest_framework                                        import generics, status
from rest_framework.response                               import Response
from rest_framework.permissions                            import DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.backends                     import TokenBackend
from rest_framework_simplejwt.serializers                  import TokenObtainPairSerializer
from hackcodev.models.reportes_encontrada                  import Reportes_Encontrados
from hackcodev.serializers.reportes_encontrada_serializers import Reportes_Encontrada_Serializer


class ReportesEncontradosCreateAPIView(generics.CreateAPIView): 
    
    # permission_classes = (IsAuthenticated,)
    # permission_classes = [IsAdminUser]
    queryset = Reportes_Encontrados.objects.all()
    serializer_class = Reportes_Encontrada_Serializer

    def post(self, request, *args, **kwargs): # metodo HTTP (POST, GET, PUSH, DELETE) 
                                    # recibe una data en el request del body 
                                    # *args argumentos basicos del servicio web 
                                    # **kwargs argumentos que se necesiten y que puedan llegar 
        print("request:", request)
        print("Args", args)
        print("Kwargs", kwargs)

        serializer = Reportes_Encontrada_Serializer(data=request.data)
        
        """Validation tocken

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReportesEncontradosAPIView(generics.ListAPIView):

    queryset = Reportes_Encontrados.objects.all()
    serializer_class = Reportes_Encontrada_Serializer
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        print("Request:", request)
        print("Args", args)
        print("Kwargs", kwargs)

        """Validation tocken 

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""

        queryset = self.get_queryset()
        serializer = Reportes_Encontrada_Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReportesEncontradosDetailAPIView(generics.RetrieveAPIView):

    queryset = Reportes_Encontrados.objects.all()
    serializer_class = Reportes_Encontrada_Serializer
    # permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        
        print("Request:", request)
        print("Args", args)
        print("Kwargs", kwargs)

        """Validation tocken 

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""

        # kwargs.append({'HTTP_AUTHORIZATION':'Bearer '+token,})  
        return super().get(request, *args, **kwargs)
class ReportesEncontradosUpdateAPIView(generics.RetrieveUpdateAPIView):
    
    queryset = Reportes_Encontrados.objects.all()
    serializer_class = Reportes_Encontrada_Serializer
    # permission_classes = (IsAuthenticated,)
    # permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        
        print("Request:", request)
        print("Args", args)
        print("Kwargs", kwargs)

        """Validation tocken && Validation if it is AdminUser

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
  
        return super().update(request, *args, **kwargs)
    
class ReportesEncontradosDeleteAPIView(generics.RetrieveDestroyAPIView):
    
    queryset = Reportes_Encontrados.objects.all()
    serializer_class = Reportes_Encontrada_Serializer
    # permission_classes = (IsAuthenticated,)
    # permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args", args)
        print("Kwargs", kwargs)
    
        """Validation tocken

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
            
        return super().destroy(request, *args, **kwargs)
    