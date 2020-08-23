from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path(r'index/',views.IndexView.as_view(),name="index"),
    path('create/', views.UserCreateView.as_view(),name="create"), # 追記
]
