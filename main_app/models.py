from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
        name = models.CharField(max_length=100)
        breed = models.CharField(max_length=100)
        description = models.TextField(max_length=250)
        age = models.IntegerField()

        def __str__(self):
            return self.name

        def get_absolute_url(self):
            return reverse('detail', kwargs={'cat_id': self.id})





# finches = [
#     Finch('Gref', 'Green Warbler Finch', 'Warble Weeble', 3),
#     Finch('Gryfie', 'Grey Warbler Finch', 'Warble warble', 4),
#     Finch('Monfie', 'Mongrove Finch', 'Hates Tuesgroves', 10),
#     Finch('Smalf', 'Small Tree Finch', 'Hates Big trees', 0),
# ]