from django.urls import path
from tba_app import views
from django.views.generic import TemplateView

urlpatterns=[
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('reg/',TemplateView.as_view(template_name='reg.html'),name='reg'),
    path('logins/',TemplateView.as_view(template_name='login.html'),name='login'),
  
    path('editprofile/',TemplateView.as_view(template_name='lawyerhome.html'),name='lawyerhome'),
    path('registration', views.register,name='register'),
    path('adminhome/', views.viewreg,name='adminhome'),
    path('view/', views.approve,name='appro'),
    path('authentication/', views.authentication,name='log'),
    path('member/', views.viewpublic,name='member'),
    path('aprovingreg/', views.viewaproving,name='aprovingreg'),
    path('contacts/', views.contacts,name='cot'),
    path('cont/', views.viewcontact,name='cont'),
    path('message/', views.on,name='status'),
    path('profileview/', views.viewprofile,name='profileview'),
    path('editprofileview/', views.editviewprofile,name='editprofile'),
    path('edit/', views.edit,name='editpro'),
 ]