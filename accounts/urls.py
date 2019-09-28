from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'accounts'

# url patterns
urlpatterns = [
    path('logout/', views.logout_user, name="logout"),
    url(r'^register/$', views.register_account, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^complete-profile/$', views.complete_profile, name='complete_profile'),
    url(r'^edit-profile/$', views.edit_profile, name='edit_profile'),
]