from django.urls import path
from Pala import views


urlpatterns = [
    path('s1/',views.s1),
    path('s2/',views.s2),
    path('t/',views.data_time),
    path('',views.home),
    path('add',views.add),
    path('emp/',views.emp_details),
    path("my/",views.my_details),

]
