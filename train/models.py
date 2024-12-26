from django.db import models
from django.contrib.auth.models import User

class train(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.name
