from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='archive'),
    path('contract/<int:contract_id>/', views.get_contract, name='get_contract'),
]