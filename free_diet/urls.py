from .views import FreeDietView
from django.urls import path

app_name = 'free_diet_app'

urlpatterns = [
    path('getfreediet/', FreeDietView.as_view(), name='free_diet_view')
]