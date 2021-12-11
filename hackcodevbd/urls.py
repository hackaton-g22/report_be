"""hackcodevbd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from hackcodev import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    
    # REPORTES ENCONTRADA 
    path('reporte_encontrada/', views.ReportesEncontradosCreateAPIView.as_view()),
    path('reporte_encontradaLista/', views.ReportesEncontradosAPIView.as_view()),
    path('reporte_encontrada/<int:pk>/', views.ReportesEncontradosDetailAPIView.as_view()),
    path('reporte_encontrada/update/<int:pk>', views.ReportesEncontradosUpdateAPIView.as_view()),
    path('reporte_encontrada/remove/<int:pk>/', views.ReportesEncontradosDeleteAPIView.as_view()),
  
  # DESAPARECIDOS
    path('desaparecido/', views.DesaparecidosCreateView.as_view()),
    path('desaparecido/<int:pk>/', views.DesaparecidosDetailView.as_view()),
    path('desaparecidoLista/', views.DesaparecidosListView.as_view()),
    
    # CASO CERRADO 
     path('caso_cerrado/', views.CasoCerradoCreateAPIView.as_view()),
    path('caso_cerradoLista/', views.CasoCerradoAPIView.as_view()),
    path('caso_cerrado/<int:pk>/', views.CasoCerradoDetailAPIView.as_view()),
    path('caso_cerrado/update/<int:pk>', views.CasoCerradoUpdateAPIView.as_view()),
    path('caso_cerrado/remove/<int:pk>/', views.CasoCerradoDeleteAPIView.as_view()),

]
