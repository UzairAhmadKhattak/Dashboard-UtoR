from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    plan = models.CharField(choices=[('0 dollars','0 dollars'),
                                 ('10 dollars','10 dollars'),
                                 ('25 dollars','25 dollars')],
                                default='0 dollars',
                                max_length=15
                                )
    def __str__(self):
        return f"plan - {self.plan}"
    
class App(models.Model):
    app_name = models.CharField(max_length=30)
    app_description = models.CharField(max_length=500)
    plan = models.ForeignKey(Plan,on_delete=models.DO_NOTHING,default=1)
    plan_subscribed_at = models.DateField(auto_now=True)
    plan_status = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    def __str__(self):
        return f"app - {self.app_name} - user - {self.user.username}"
