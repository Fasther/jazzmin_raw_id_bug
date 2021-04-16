

from django.db.models import Model, ForeignKey, CASCADE

# Create your models here.
from django.db.models import CharField


class Company(Model):
    name = CharField(max_length=64)

    def __str__(self):
        return self.name


class Worker(Model):
    company = ForeignKey(Company, on_delete=CASCADE)
    name = CharField(max_length=64)
    supervisor = ForeignKey('self', on_delete=CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
