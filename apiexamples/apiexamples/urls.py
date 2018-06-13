from django.contrib import admin
from django.urls import path
from apimore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.geo, name='geo'),
    # path('oxford/', views.oxford, name='oxford'),
]
