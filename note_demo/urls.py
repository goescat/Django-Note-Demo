"""note_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import account.views
import note.views


urlpatterns = [
    url(r'^$', account.views.home, name='home'),
    url('account/', include('account.urls')),
    url('account/', include('django.contrib.auth.urls')),
    url(r'^note/', note.views.note, name='note'),
    url(r'^delete_note/(?P<note_id>[0-9]+)/$', note.views.delete_note),
    url(r'^django_admin/', admin.site.urls),
]
