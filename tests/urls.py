from __future__ import absolute_import, division, print_function

from django.urls import include, re_path
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from rest_framework_docs.views import DRFDocsView
from tests import views

accounts_urls = [
    re_path(r'^login/$', views.LoginView.as_view(), name="login"),
    re_path(r'^login2/$', views.LoginWithSerilaizerClassView.as_view(), name="login2"),
    re_path(r'^register/$', views.UserRegistrationView.as_view(), name="register"),
    re_path(r'^reset-password/$', view=views.PasswordResetView.as_view(), name="reset-password"),
    re_path(r'^reset-password/confirm/$', views.PasswordResetConfirmView.as_view(), name="reset-password-confirm"),

    re_path(r'^user/profile/$', views.UserProfileView.as_view(), name="profile"),

    re_path(r'^test/$', views.TestView.as_view(), name="test-view"),
]

organisations_urls = [
    re_path(r'^create/$', view=views.CreateOrganisationView.as_view(), name="create"),
    re_path(r'^(?P<slug>[\w-]+)/members/$', view=views.OrganisationMembersView.as_view(), name="members"),
    re_path(r'^(?P<slug>[\w-]+)/leave/$', view=views.LeaveOrganisationView.as_view(), name="leave"),
    re_path(r'^(?P<slug>[\w-]+)/errored/$', view=views.OrganisationErroredView.as_view(), name="errored"),
    re_path(r'^(?P<slug>[\w-]+)/$', view=views.RetrieveOrganisationView.as_view(), name="organisation"),
]

router = SimpleRouter()
router.register('organisation-model-viewsets', views.TestModelViewSet, base_name='organisation')

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^docs/', DRFDocsView.as_view(drf_router=router), name='drfdocs'),

    # API
    re_path(r'^accounts/', view=include((accounts_urls, "accounts"), namespace='accounts')),
    re_path(r'^organisations/', view=include((organisations_urls, "organisations"), namespace='organisations')),
    re_path(r'^', include(router.urls)),

    # Endpoints without parents/namespaces
    re_path(r'^another-login/$', views.LoginView.as_view(), name="login"),
]
