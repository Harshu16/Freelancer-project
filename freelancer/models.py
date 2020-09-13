from django.db import models

class Freelancer(models.Model):
    free_id = models.AutoField(primary_key=True)
    free_name = models.CharField(max_length=50)
    free_domain = models.CharField(max_length=50)
    free_phone = models.CharField(max_length=50, default="")
    free_email = models.EmailField(max_length=50, default="")
    free_password1 = models.CharField(max_length=50)
    free_password2 = models.CharField(max_length=50)

    def __str__(self):
        return self.free_name


from django.db import models

# Create your models here.
