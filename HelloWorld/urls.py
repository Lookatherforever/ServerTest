from django.urls import path
from .views import hello_world

app_name = 'Hello_World'
urlpatterns = [
    path("helloworld/", hello_world, name="hello_world"),
]