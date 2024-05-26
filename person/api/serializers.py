from rest_framework.serializers import ModelSerializer
from person.models import Person, TypeIdentification

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
    
class TypeIdentificationSerializer(ModelSerializer):
    class Meta:
        model = TypeIdentification
        fields = '__all__'