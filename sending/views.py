from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from sending.forms import ClientForm, MailingForm, MessageForm
from sending.models import Client, Mailing, Message
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ClientListView(ListView):
    model = Client

    # def get_queryset(self):
    #    return get_clients_from_cache()
    """def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter()
        return queryset"""

    def get_context_data(self, *args, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for client in context_data['object_list']:
            active_version = Client.objects  # .first()
            client.active_version = active_version
        return context_data


class ClientDetailView(DetailView):
    model = Client

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        # self.object.views_counter += 1
        # self.object.save()
        return self.object


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    # fields = ("email", "fio", "comment")
    success_url = reverse_lazy('sending:list_client')

    def form_valid(self, form):
        client = form.save()
        # user = self.request.user
        # client.owner = user
        client.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    # fields = ("name", "description", "photo", "category", "price", "created_at", "updated_at", "manufactured_at")
    success_url = reverse_lazy('sending:list_client')

    def get_success_url(self):
        return reverse('sending:list_client')  # , args=[self.kwargs.get('pk')]

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        """ClientFormset = inlineformset_factory(Client,)  # Version, VersionForm, extra=1
        if self.request.method == 'POST':
            context_data["formset"] = ClientFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ClientFormset(instance=self.object)"""
        return context_data

    """def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))"""


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('sending:list_client')


# -----------------------------------------------------------------------------------
#  Mailing

class MailingListView(ListView):
    model = Mailing

    # def get_queryset(self):
    #    return get_clients_from_cache()
    """def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter()
        return queryset"""

    def get_context_data(self, *args, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for mailing in context_data['object_list']:
            active_version = Mailing.objects  # .first()
            mailing.active_version = active_version
        return context_data


class MailingDetailView(DetailView):
    model = Mailing

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        # self.object.views_counter += 1
        # self.object.save()
        return self.object


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    # fields = ("email", "fio", "comment")
    success_url = reverse_lazy('sending:list_mailing')

    def form_valid(self, form):
        mailing = form.save()
        # user = self.request.user
        # client.owner = user
        mailing.save()

        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    # fields = ("name", "description", "photo", "category", "price", "created_at", "updated_at", "manufactured_at")
    success_url = reverse_lazy('sending:list_mailing')

    def get_success_url(self):
        return reverse('sending:list_mailing')  # , args=[self.kwargs.get('pk')]

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        """ClientFormset = inlineformset_factory(Client,)  # Version, VersionForm, extra=1
        if self.request.method == 'POST':
            context_data["formset"] = ClientFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ClientFormset(instance=self.object)"""
        return context_data


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('sending:list_mailing')


# -----------------------------------------------------------------------------------
#  Message

class MessageListView(ListView):
    model = Message

    # def get_queryset(self):
    #    return get_clients_from_cache()
    """def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter()
        return queryset"""

    def get_context_data(self, *args, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for message in context_data['object_list']:
            active_version = Message.objects  # .first()
            message.active_version = active_version
        return context_data


class MessageDetailView(DetailView):
    model = Message

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        # self.object.views_counter += 1
        # self.object.save()
        return self.object


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('sending:list_message')

    def form_valid(self, form):
        message = form.save()
        # user = self.request.user
        # client.owner = user
        message.save()

        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('sending:list_message')

    def get_success_url(self):
        return reverse('sending:list_message')  # , args=[self.kwargs.get('pk')]

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('sending:list_message')
