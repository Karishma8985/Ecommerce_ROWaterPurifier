from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_months = models.IntegerField(help_text="Duration in months")
    pics = models.ImageField(upload_to='servicesimage')

    def __str__(self):
        return self.title
