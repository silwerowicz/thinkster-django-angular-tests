from django.conf.urls import patterns, url

from thinkster_django_angular_boilerplate.views import IndexView

from rest_framework_nested import routers
from authentication.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',

    url(r'^api/v1/', include(routers.urls)),

    url('^.*$', IndexView.as_view(), name='index'),
)
'''
It is very important that the last URL in the above snippet always be the last URL.
This is known as a passthrough or catch-all route. It accepts all requests not matched by a previous rule and passes the
request through to AngularJS's router for processing. The order of other URLS is normally insignificant.

'''