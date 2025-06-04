from django.db import models
from datetime import datetime

class Nota(models.Model):
    """
    Model representing a note in the Notes App.

    Attributes:
        title (str): The title of the note.
        description (str): The detailed description of the note.
        created_at (datetime): The date and time when the note was created.
        deadline (date): The deadline for the note.
        finished_at (datetime, optional): The date and time when the note was finished.
    """
    title = models.CharField(
        max_length=50, verbose_name="Titulo", null=False, blank=False
    )
    description = models.TextField(max_length=1000, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ["-created_at"]

    def concluir_nota(self):
        if not self.finished_at:
            self.finished_at = datetime.now()
