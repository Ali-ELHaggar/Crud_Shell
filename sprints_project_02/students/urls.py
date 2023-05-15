from django.urls import path
from . import views
from .views import StudentCreate
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_view, name='list_view'),
    path('create', StudentCreate.as_view()),
    path('home/',views.home_view,name='home'),
    path('home2/',views.home_view2,name='home2'),
    path('admin/', admin.site.urls),

]


