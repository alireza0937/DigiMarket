from django.urls import path
from .views import RegisterCreateView, SubmitSellerProfileCreateView

urlpatterns = [
    path("api/register/", RegisterCreateView.as_view(), name="register-api-view"),
    path("api/seller/profile/", SubmitSellerProfileCreateView.as_view(), name="sellerproflie-api-view")

]
