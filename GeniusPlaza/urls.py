from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from django.views.defaults import page_not_found
from django.conf.urls import handler404 , handler500
from django.shortcuts import render, redirect, HttpResponse, Http404










app_name = 'GeniusPlaza'


admin.site.site_title = "GeniusPlaza"

urlpatterns = [
    url(r'^management/administration', admin.site.urls),
    # url('apih/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^RecipeApi/', include('Recipe.urls')),



]


# handler404 = 'Account.views.handler404'
# handler500 = 'Account.views.handler500'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
