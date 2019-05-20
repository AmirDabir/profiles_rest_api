from django.conf.urls import url
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello_viewset',views.Helloviewset,base_name='hello_viewset_base_name')

urlpatterns = [
      url(r'^hello_api',views.Helloapiview.as_view()), #Apiview url
      url(r'',include(router.urls)) #Viewset url


]
