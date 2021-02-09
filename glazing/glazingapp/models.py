from django.db import models


class contact(models.Model):
    Name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Message from  ' + self.Name + '-' + self.email


class works_model(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    Images = models.ImageField(upload_to="glazingapp/images", default="")
    status = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.title


class services(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    Images = models.ImageField(upload_to="glazingapp/images", default="")

    def __str__(self):
        return self.title
