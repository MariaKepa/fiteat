from django.conf.urls import url
from .import views
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    
    url(r'^$', views.first_page, name='first_page'),
    url(r'^product/$', views.product, name='product'),
    url(r'^product/(?P<id>[0-9]+)$', views.product_detail, name='product_detail'),
    url(r'^contact/$', views.aboutme, name= 'aboutme'),
    url(r'^statute/$', views.statute, name = 'statute'),
    url(r'^tips/', views.tips, name='tips'),
    url(r'^aboutme/$', views.contact , name = 'contact'),
    url(r'^dairy/$', views.dairy , name = 'dairy'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', login , name ='login'),
    url(r'^dashboard/$', views.dashboard, name = 'dashboard'),
    url(r'^logout_then_login/$', logout_then_login, name = 'logout_then_login'), 
    url(r'^body_weight/$', views.body_weight, name = 'body_weight'),
    url(r'^edit_panel/$', views.edit_panel, name = 'edit_panel'),

]

