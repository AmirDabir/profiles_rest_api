from django.conf.urls import url
from . import views

urlpatterns = [
      url(r'^hello_api',views.Helloapiview.as_view())

]
