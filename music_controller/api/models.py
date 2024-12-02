from django.db import models
import string
import random

def generate_unique_code():
    length=6

    while True:
        # Generate bunch of codes until its unique and 
        code=''.join(random.choices(string.ascii_uppercase, k=length))
        # query to check uniqueness from the exiting code
        # checking the count of list having same code if zero then perfect break.
        
        if Room.objects.filter(code=code).count()==0:
            break
    return code


# Create your models here.
class Room(models.Model):
    #Attributes
    code=models.CharField(max_length=8, default="",unique=True)
    host=models.CharField(max_length=50, unique=True,default="default_host")
    guest_can_pause=models.BooleanField(null=False,default=False)
    votes_to_skip=models.IntegerField(null=False,default=1)
    created_at=models.DateTimeField(auto_now_add=True)


    