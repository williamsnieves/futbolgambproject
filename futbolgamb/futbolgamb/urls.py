from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from maintournament.views import PrincipalViewSet
from phasea.views import PhaseAViewSet

router = routers.DefaultRouter()
router.register(r'principal', PrincipalViewSet)
router.register(r'phasea', PhaseAViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sociallogin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api/1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
