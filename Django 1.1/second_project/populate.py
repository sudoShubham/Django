import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')
import django
django.setup()
import random
from second_app.models import User
from faker import Faker
fakegen = Faker()

def add_records(N=5):
    for entry in range(N):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.email()

        rec = User.objects.get_or_create(first_name=first_name,last_name=last_name,email=email)


if __name__=='__main__':
    print("Populating....")
    add_records(20)
    print('Done')
