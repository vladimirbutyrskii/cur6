from django.urls import path
from sending.apps import SendingConfig
from sending.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    MailingCreateView, MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView, MessageCreateView, \
    MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView

app_name = SendingConfig.name

urlpatterns = [

    path("create_client", ClientCreateView.as_view(), name="create_client"),
    path("list_client", ClientListView.as_view(), name='list_client'),
    path("view_client/<int:pk>/", ClientDetailView.as_view(), name='view_client'),
    path("update_client/<int:pk>/", ClientUpdateView.as_view(), name='update_client'),
    path("delete_client/<int:pk>/", ClientDeleteView.as_view(), name="delete_client"),

    path("create_mailing", MailingCreateView.as_view(), name="create_mailing"),
    path("list_mailing", MailingListView.as_view(), name='list_mailing'),
    path("view_mailing/<int:pk>/", MailingDetailView.as_view(), name='view_mailing'),
    path("update_mailing/<int:pk>/", MailingUpdateView.as_view(), name='update_mailing'),
    path("delete_mailing/<int:pk>/", MailingDeleteView.as_view(), name="delete_mailing"),

    path("create_message", MessageCreateView.as_view(), name="create_message"),
    path("list_message", MessageListView.as_view(), name='list_message'),
    path("view_message/<int:pk>/", MessageDetailView.as_view(), name='view_message'),
    path("update_message/<int:pk>/", MessageUpdateView.as_view(), name='update_message'),
    path("delete_message/<int:pk>/", MessageDeleteView.as_view(), name="delete_message"),

]