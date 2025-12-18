from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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


# One to Many

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVerity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return f'{self.user.username} reviews for {self.chai.name}'


# Many to Many

class Store(models.Model): 
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_verities = models.ManyToManyField(ChaiVerity, related_name='stores')

    def __str__(self): 
        return self.name
    

#One to One

class ChaiCertificate(models.Model): 
    chai = models.OneToOneField(ChaiVerity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()


    def __str__(self): 
        return f'Certificate for {self.name.chai}'
    
