
from django.db import models

class PredictionHistory(models.Model):

    image = models.ImageField(
        upload_to="predictions/"
    )

    disease = models.CharField(
        max_length=255
    )

    confidence = models.FloatField()

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.disease

