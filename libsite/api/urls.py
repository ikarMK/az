"""libsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import BookView,AuthorView,PublisherView
from cacheops import cached, cached_view
app_name = "book"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('book/', BookView.as_view()),
    path('book/<int:pk>', BookView.as_view()),
    path('author/', AuthorView.as_view()),
    path('author/<int:pk>', AuthorView.as_view()),
    path('publisher/', PublisherView.as_view()),
    path('publisher/<int:pk>', PublisherView.as_view()),
]
