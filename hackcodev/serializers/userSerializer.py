from rest_framework import serializers
from hackcodev.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','us_nombre','us_apellido','us_entidad','us_telefono','us_ciudad','us_direccion','password']