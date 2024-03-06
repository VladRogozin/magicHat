from django.db import models

class PDFPage(models.Model):
    page_number = models.IntegerField()
    text_with_markup = models.TextField()

    def __str__(self):
        return f"Страница {self.page_number}"

