from django.db import models

'''
this is a model for client have many fields user(related at user of django)
name,logo and country (related at country  model)
'''
class Client(models.Model):
    name=models.CharField(max_length=20)
    logo=models.FileField(upload_to='Logos')
    country=models.ForeignKey('Country',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)




'''
it is country model have many fields name and flag 
'''
class Country(models.Model):
    name=models.CharField(max_length=25)
    flag=models.FileField(upload_to='Flages')

    def __str__(self):
        return self.name