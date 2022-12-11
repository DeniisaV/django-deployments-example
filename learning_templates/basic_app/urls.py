from django.urls import path, include
from basic_app import views

#FOR TEMPLATE TAGGING
app_name = 'basic_app'   #mereu trebuie sa avem variabila cu numele app_name, sa ii asignam numele aplicatiei

urlpatterns = [
   path('relative/', views.relative,name='relative'),  #url pt view-ul relative (adica daca avem domainname/basic_app/relative)
   path('other/', views.other, name='other'), #url pt view-ul other
]
