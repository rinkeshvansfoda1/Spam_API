from rest_framework import serializers
from .models import Contact

#  a Serializer is the way to convert complex data types, such as database querysets and model instances, into JSON, XML

# it is used to get all the object fields from table called Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'

# it is used to get id,name,mobile_no fields from table called Contact
class ContactSerialized(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['id','name','mobile_no']