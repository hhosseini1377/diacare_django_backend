from .views import FreeDietView, AddFreeDiet
from django.urls import path

app_name = 'free_diet_app'

urlpatterns = [
    path('getfreediet/', FreeDietView.as_view(), name='free_diet_view'),
    path('addfreediet/', AddFreeDiet.as_view(), name='add_free_diet'),

]