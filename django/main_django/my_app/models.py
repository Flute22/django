from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVerity(models.Model): 
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala Chai'),
        ('GN', 'Ginger Chai'),
        ('KS', 'Kasir Chai'),
        ('PL', 'Plain Chai'),
        ('EL', 'Elichi Chai'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self): 
        return self.name 