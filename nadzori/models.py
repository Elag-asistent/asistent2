from projekti.models import Stanja
from projekti.models import Openclose
from django.db import models

# Create your models here.
#class Stanja(models.Model):
#    stanje = models.CharField(max_length=50)
#    def __unicode__(self):
#        return self.stanje
#
#class Openclose(models.Model):
#    oc = models.CharField(max_length=50)
#    def __unicode__(self):
#        return self.oc

class Nadzor(models.Model):
    imenovanje = models.CharField(unique=True, max_length=200)
    gradevina = models.CharField(blank=True, max_length=200)
    narucitelj = models.CharField(blank=True, max_length=200)
    investitor = models.CharField(blank=True, max_length=200)
    opis = models.CharField(blank=True, max_length=200)
    nadzorni_inzenjer = models.CharField(blank=True, max_length=50)
    kontakt = models.CharField(blank=True, max_length=50)
    zavrsno_izvjesce = models.CharField(blank=True, max_length=100)
    datum_tehnickog_pregleda = models.DateField(blank=True, null=True)
    ponuda = models.CharField(blank=True, max_length=100)
    racun = models.CharField(blank=True, max_length=200)
    uplata = models.CharField(blank=True, max_length=200)
    saldo = models.CharField(blank=True, max_length=20)
    stanje = models.ForeignKey(Stanja, default=1)
    biljeska = models.CharField(blank=True, max_length=200)
    nadzor = models.ForeignKey(Openclose, default=1)
    def __unicode__(self):
        return self.imenovanje
