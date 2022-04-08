from django.urls import path

from account.views import (
    Login, Logout, does_account_exist_view, RegisterView, ChangePasswordView,
    UpdateProfileView, GetProfileView
)
app_name = 'account'

urlpatterns = [
    path('check_if_account_exists/', does_account_exist_view, name="check_if_account_exists"),
    path('register/', RegisterView.as_view(), name='sign-up'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    # path('login/phone/', LoginPhone.as_view(), name='login-phone')
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('show_profile/<int:pk>/', GetProfileView.as_view(), name='auth_show_profile'),

]
