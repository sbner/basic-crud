from django.contrib import admin
from django.urls import path
from notes.views import (
    NotasListView,
    NotasCreateView,
    NotasUpdateView,
    NotasDeleteView,
    NotaCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", NotasListView.as_view(), name="lista_notas"),
    path("create", NotasCreateView.as_view(), name="notas_create"),
    path("update/<int:pk>", NotasUpdateView.as_view(), name="atualizar_nota"),
    path("delete/<int:pk>", NotasDeleteView.as_view(), name="deletar_nota"),
    path("complete/<int:pk>", NotaCompleteView.as_view(), name="concluir_nota"),
]
