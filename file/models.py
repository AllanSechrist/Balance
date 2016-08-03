from django.db import models
from django.core.urlresolvers import reverse


class Folder(models.Model):
    name = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('file:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Receipt(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    store = models.CharField(max_length=250)
    date = models.CharField(max_length=15)
    # i.e car upkeep, groceries, rent, water bill...ect, ect
    classification = models.CharField(max_length=250)

    def __str__(self):
        return self.store + ' date: ' + self.date
