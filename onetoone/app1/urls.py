from django.urls import path
from .views import empView, roleView,empdataView,updateView,deleteView


urlpatterns = [

    path('', empView, name='empview'),
    path('role/', roleView, name='roleview'),
    path('data/', empdataView, name = 'empdataview'),
    path('update/<int:id>/', updateView, name = 'updateview' ),
    path('delete/<int:id>/', deleteView, name= 'deleteview' )


]