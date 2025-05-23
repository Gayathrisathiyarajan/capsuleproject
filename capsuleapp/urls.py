from django.urls import path
from .views import *
urlpatterns = [
    path('', CapsuleInsertUpdateView, name='CapsuleInsertUpdateView'),
    path('CapsuleDeleteView/', CapsuleDeleteView, name='CapsuleDeleteView'),
]
