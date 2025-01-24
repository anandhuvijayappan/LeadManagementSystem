from django.db import models

# Create your models here.

class Lead(models.Model):

    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15)

    STATUS_CHOICES=(
        ("New","New"),
        ("In Progress","In Progress"),
        ("Converted","Converted"),
        ("Rejected","Rejected")
    )

    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default="New")

    SOURCE_CHOICES=(
        ("Online","Online"),
        ("Referral","Referral"),
        ("Event","Event"),
        ("Advertisement","Advertisement")
    )

    source=models.CharField(max_length=100,choices=SOURCE_CHOICES,default="Advertisement")

    def __str__(self):
        return self.name