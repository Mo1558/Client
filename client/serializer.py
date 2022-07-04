from rest_framework import serializers
from . models import Client,Country

'''
this serializer for serialize the data of client model
in all fields
'''
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client        #model
        fields='__all__'    #All fields of client model



'''
this serializer for serialize the data of country model
in all fields
'''
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country        #model
        fields='__all__'    #All fields of country model



'''
this serializer for serialize the data of country model 
and country model to appear country data not id 
in all fields
'''
class ClientViewSerializer(serializers.ModelSerializer):
    country=CountrySerializer()
    class Meta:
        model=Client        #model
        fields='__all__'    #All fields of client model




