from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Nota
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime


class NotasListView(ListView):
    model = Nota


class NotasCreateView(CreateView):
    model = Nota
    fields = ["title", "description", "deadline"]
    success_url = reverse_lazy("lista_notas")


class NotasUpdateView(UpdateView):

    model = Nota
    fields = ["title", "description", "deadline"]
    success_url = reverse_lazy("lista_notas")


class NotasDeleteView(DeleteView):
    model = Nota
    success_url = reverse_lazy("lista_notas")


class NotaCompleteView(View):
    """
    View to mark a Note as complete.
    Redirects to the notes list view after completion.
    """
    def get(self, request, pk):
        nota = get_object_or_404(Nota, pk=pk)
        nota.concluir_nota()
        nota.save()
        return redirect("lista_notas")
