from django.urls import path

# . means current directory, current package (hello folder)
from . import views

urlpatterns = [

    # views is the module imported in line 4
    # the name in the funcion in views is index
    path("", views.index)


]