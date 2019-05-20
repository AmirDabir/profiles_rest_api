from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import include


router = DefaultRouter()

router.register('hello_viewset',views.Helloviewset,base_name='hello_viewset_base_name')
router.register('profile',views.Userprofileviewset)

urlpatterns = [
      url(r'^hello_api',views.Helloapiview.as_view()), #Apiview url
      url(r'',include(router.urls)) #Viewset url

]
