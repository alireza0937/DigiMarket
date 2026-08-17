from django.urls import path
from .views import RegisterCreateView

urlpatterns = [
    path("api/register/", RegisterCreateView.as_view(), name="register-api-view")
]
