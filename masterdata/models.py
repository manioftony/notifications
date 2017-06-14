from django.db import models

# Create your models here.
ACTIVE = ((0,'Inactive'), (2, 'Active'),)

class Base(models.Model):
    
    """ Basic Fields """

    active = models.PositiveIntegerField(choices = ACTIVE, default=2)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)

    def switch(self):
        self.active = {0: 2, 2: 0}[self.active]
        self.save()
        return self.active

    class Meta:
        abstract = True





class Student(Base):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name