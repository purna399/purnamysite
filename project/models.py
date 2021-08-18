from django.db import models

class studentdetails(models.Model):
    name = models.CharField(max_length=20)
    mobile= models.CharField(max_length=20)
    email =  models.CharField(max_length=20)
    age = models.IntegerField()
    address=models.TextField()
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        db_table='personal_info'