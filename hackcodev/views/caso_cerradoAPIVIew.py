from rest_framework                                        import generics, status
from rest_framework.response                               import Response
from rest_framework.permissions                            import DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.backends                     import TokenBackend
from rest_framework_simplejwt.serializers                  import TokenObtainPairSerializer
from hackcodev.models.caso_cerrado_model                   import Caso_Cerrado
from hackcodev.serializers.caso_cerrado_serializer         import Caso_Cerrado_Serializer


class CasoCerradoCreateAPIView(generics.CreateAPIView): 
    
    # permission_classes = (IsAuthenticated,)
    # permission_classes = [IsAdminUser]
    queryset = Caso_Cerrado.objects.all()
    serializer_class = Caso_Cerrado_Serializer

    def post(self, request, *args, **kwargs): # metodo HTTP (POST, GET, PUSH, DELETE) 
                                    # recibe una data en el request del body 
                                    # *args argumentos basicos del servicio web 
                                    # **kwargs argumentos que se necesiten y que puedan llegar 
        print("request:", request)
        print("Args", args)
        print("Kwargs", kwargs)

        serializer = Caso_Cerrado_Serializer(data=request.data)
        
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

class CasoCerradoAPIView(generics.ListAPIView):

    queryset = Caso_Cerrado.objects.all()
    serializer_class = Caso_Cerrado_Serializer
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
        serializer = Caso_Cerrado_Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CasoCerradoDetailAPIView(generics.RetrieveAPIView):

    queryset = Caso_Cerrado.objects.all()
    serializer_class = Caso_Cerrado_Serializer
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
class CasoCerradoUpdateAPIView(generics.RetrieveUpdateAPIView):
    
    queryset = Caso_Cerrado.objects.all()
    serializer_class = Caso_Cerrado_Serializer
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
    
class CasoCerradoDeleteAPIView(generics.RetrieveDestroyAPIView):
    
    queryset = Caso_Cerrado.objects.all()
    serializer_class = Caso_Cerrado_Serializer
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
    