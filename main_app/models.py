from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# Create your models here.
class Finch(models.Model):
        name = models.CharField(max_length=100)
        breed = models.CharField(max_length=100)
        description = models.TextField(max_length=250)
        age = models.IntegerField()

        def __str__(self):
            return self.name

        def get_absolute_url(self):
            return reverse('detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'

    class Meta:
        ordering = ['-date']

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toy_detail', kwargs={'pk': self.id})



# finches = [
#     Finch('Gref', 'Green Warbler Finch', 'Warble Weeble', 3),
#     Finch('Gryfie', 'Grey Warbler Finch', 'Warble warble', 4),
#     Finch('Monfie', 'Mongrove Finch', 'Hates Tuesgroves', 10),
#     Finch('Smalf', 'Small Tree Finch', 'Hates Big trees', 0),
# ]