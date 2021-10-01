from django.db import models
from django.urls import reverse
# Create your models here.
class MainSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Sector(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Stat(models.Model):
    title = models.CharField(max_length=300)
    number = models.IntegerField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('landinpage:portofolio', args=[self.title])


class Project(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=150)
    client = models.CharField(max_length=150)
    project_date = models.DateField(auto_now=False, auto_now_add=False)
    project_url = models.URLField(max_length=250, blank=True)
    project_img = models.ImageField(upload_to='projects')

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=250)
    fonction = models.CharField(max_length=200)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='team')
    team_img = models.ImageField(upload_to='team')   

    def __str__(self):
        return self.name


class BucoInfo(models.Model):
    adress = models.CharField(max_length=150)
    mail = models.EmailField(max_length=254)
    # num = models.PhoneNumberField()

    def __str__(self):
        return f"Buco information"
    