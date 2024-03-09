# ihaUygulamasi/models.py

from django.db import models
from django.contrib.auth.models import User

class IHA(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    agirlik = models.FloatField()
    kategori = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.marka} {self.model}"

class Kiralama(models.Model):
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE)
    tarih_baslangic = models.DateTimeField()
    tarih_bitis = models.DateTimeField()
    kiralayan_uye = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.iha} - {self.tarih_baslangic} - {self.tarih_bitis}"
