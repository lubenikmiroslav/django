# recepty/models.py

from django.db import models

class Kuchar(models.Model):
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    fotografie = models.ImageField(upload_to='autori/', blank=True, null=True)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Kategorie(models.Model):
    nazev = models.CharField(max_length=50)

    def __str__(self):
        return self.nazev

class Recept(models.Model):
    nazev = models.CharField(max_length=100)
    obsah = models.TextField()
    doba_pripravy = models.PositiveIntegerField()
    kuchar = models.ForeignKey(Kuchar, on_delete=models.CASCADE, related_name='recepty')
    kategorie = models.ManyToManyField(Kategorie)
    obrazek = models.ImageField(upload_to='obalky/', blank=True, null=True)

    def __str__(self):
        return self.nazev

# Pokud HODNOCENÍ opravdu nechceš používat, nepřidávej ho do importu nikde
