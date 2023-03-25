from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=200, null=True)
    location = models.TextField(null=True)
    def __str__(self):
       return self.name + " " + self.email + " " + self.location




   
class Team(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(null=True)
    role = models.CharField(max_length=200, null=True)
    
    def __str__(self):
       return self.name + " " + self.email + " " + self.role 
   
class Contact(models.Model):
    user = models.ForeignKey(Team,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    desc = models.TextField(max_length=5000, null=True)
    image = models.ImageField(null=True,blank=True,upload_to="static/")
    
    class Meta:
        verbose_name_plural = "Contacts"
    

    
