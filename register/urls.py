from django.urls import path,include
from . import views

urlpatterns=[
    path('home/',views.home),
    path('registration/',views.registration),
    path('login/',views.login),
    path('login_page/',views.login_page),
    # path('success/',views.success),




]