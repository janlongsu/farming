from django.conf.urls import url,include
from . import  views
#import blog.views as bv
urlpatterns = [
    url(r'^$', views.index),
]
