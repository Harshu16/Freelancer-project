from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=50,unique= True,default="")
    client_phone = models.CharField(max_length=50, default="")
    client_email = models.EmailField(max_length=50, default="",unique= True)
    client_password1 = models.CharField(max_length=50)
    client_password2 = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name



class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_domain = models.CharField(max_length=50, default="")
    task_rate = models.IntegerField(default="")
    name = models.ForeignKey('Client',on_delete=models.DO_NOTHING,)


    def __str__(self):
        return self.task_name


