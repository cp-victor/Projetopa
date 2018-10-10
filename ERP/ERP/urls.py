from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from BOM import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^signup/$', accounts_views.signup, name='signup'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	url(r'^post/new', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/', views.forn_detail, name='forn_detail'),

	url(r'^admin/', admin.site.urls),
]