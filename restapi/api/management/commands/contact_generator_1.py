from django.core.management.base import BaseCommand
import random
from faker import Faker
from api.models import Contact

# this file is used to generate data

class Command(BaseCommand):
    help='Generate random Contacts'
    def handle(self,*args,**kwargs):
        fake=Faker()

        for i in range(20):
            contact=Contact(
                name=fake.name(),
                email=fake.email(),
                mobile_no=fake.numerify(text='##########'),
                spam=random.choice([True,False])
            )
            contact.save()

        self.stdout.write(self.style.SUCCESS("Successfully generated contacts"))