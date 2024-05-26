from django.urls import path
from . import views

urlpatterns = [
    path('get-people', views.get_people),
    path('get-types-identification', views.get_type_identification),
    path('create-person', views.create_person),
]