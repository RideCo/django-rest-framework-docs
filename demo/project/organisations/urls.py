from django.urls import re_path
from project.organisations import views

app_name = "organisations"

urlpatterns = [
    re_path(r'^create/$', view=views.CreateOrganisationView.as_view(), name="create"),
    re_path(r'^(?P<slug>[\w-]+)/$', view=views.RetrieveOrganisationView.as_view(), name="organisation"),
    re_path(r'^(?P<slug>[\w-]+)/members/$', view=views.OrganisationMembersView.as_view(), name="members"),
    re_path(r'^(?P<slug>[\w-]+)/leave/$', view=views.LeaveOrganisationView.as_view(), name="leave")
]
