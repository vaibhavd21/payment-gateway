from django.db import models

# Create your models here.
class payment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    order_id = models.CharField(max_length=300,null=False,default="")
    payment_id = models.CharField(max_length = 300,default="")
    status = models.BooleanField(default=False)
    email = models.CharField(max_length=120,default="")
    time = models.DateTimeField(auto_now_add=True)


