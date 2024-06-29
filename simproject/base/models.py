from django.db import models
import uuid
# Create your models here.
class BaseProfile(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True