from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/', auth_views.login, name='login',
        kwargs={'redirect_authenticated_user': True}),
    url(r'^logout/', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^playbooks/', include('ansible.urls')),
]
