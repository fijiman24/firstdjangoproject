# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, calebPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('caleb/', calebPageView, name='caleb'),
    path('homePost/', homePost, name='homePost'),
    path('<int:choice>/results/', results, name='results'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
