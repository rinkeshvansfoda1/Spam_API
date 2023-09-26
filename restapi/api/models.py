from django.db import models

# Create your models here.

# using models here I had created an Table called Contact with some fields like name, email, mobile_no, spam
# spam is used to identify the spam number in the global database

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=False)
    mobile_no=models.CharField(max_length=10,unique=True)
    spam=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    # class Meta:
    #     app_label='api'