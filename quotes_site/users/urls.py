from django.urls import path

from .forms import LoginForm
from .views import RegisterView, MyLoginView, MyLogoutView

app_name = "users"

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='register'),
    path('signin/', MyLoginView.as_view(
        template_name="users/signin.html",
        authentication_form=LoginForm,
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', MyLogoutView.as_view(
        template_name="users/logout.html",
    ), name='logout'),
]
