from django.urls import path
from . import views
urlpatterns = [
    path('', views.mytodo, name='home'),
 ]