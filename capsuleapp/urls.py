from django.urls import path
from .views import *
from capsuleapp import *
urlpatterns = [
    path('', CapsuleInsertUpdateView, name='CapsuleInsertUpdateView'),
    path('CapsuleDeleteView/', CapsuleDeleteView, name='CapsuleDeleteView'),
    path('run-daily-job/secret123/', run_capsule_email, name='run_capsule_email'),  # ✅ secure endpoint
]
