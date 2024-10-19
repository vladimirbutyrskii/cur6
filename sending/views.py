from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from sending.forms import ClientForm
from sending.models import Client
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ClientListView(ListView):
    model = Client

    # def get_queryset(self):
    #    return get_clients_from_cache()

    def get_context_data(self, *args, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for client in context_data['object_list']:
            active_version = Client.objects.filter(client=client).first()
            client.active_version = active_version
        return context_data


class ClientDetailView(DetailView):
    model = Client

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    # fields = ("name", "description", "photo", "category", "price", "created_at", "updated_at", "manufactured_at")
    success_url = reverse_lazy('sending:client_list')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    # fields = ("name", "description", "photo", "category", "price", "created_at", "updated_at", "manufactured_at")
    success_url = reverse_lazy('sending:client_list')

    def get_success_url(self):
        return reverse('catalog:products_detail', args=[self.kwargs.get('pk')])

    """def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ClientFormset = inlineformset_factory(Client, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data["formset"] = ClientFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ClientFormset(instance=self.object)
        return context_data"""

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('sending:client_list')
