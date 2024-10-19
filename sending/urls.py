from django.urls import path
from sending.apps import SendingConfig
from sending.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = SendingConfig.name

urlpatterns = [

    path("create_client", ClientCreateView.as_view(), name="create_client"),
    path("list_client", ClientListView.as_view(), name='list_client'),
    path("view_client/<int:pk>/", ClientDetailView.as_view(), name='view_client'),
    path("edit_client/<int:pk>/", ClientUpdateView.as_view(), name='edit_client'),
    path("delete_client/<int:pk>/", ClientDeleteView.as_view(), name="delete_client"),
]