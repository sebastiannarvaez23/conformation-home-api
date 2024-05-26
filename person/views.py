from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db import IntegrityError
from .models import Person, TypeIdentification
from .api.serializers import PersonSerializer, TypeIdentificationSerializer

@api_view(['GET'])
def get_people(request):
    person = Person.objects.all()
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_person(request):
    data = request.data
    try: 
        person = Person.objects.create(
            is_head_household=data['is_head_household'],
            first_name=data['first_name'],
            second_name=data['second_name'],
            first_last_name=data['first_last_name'],
            second_last_name=data['second_last_name'],
            date_birth=data['date_birth'],
            type_identification=TypeIdentification.objects.get(id=data['type_identification']),
            num_identification=data['num_identification'],
        )
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)
    except IntegrityError:
        return Response({'msn_client': 'La persona con el número de identificación ingresado ya existe.'}, status=status.HTTP_400_BAD_REQUEST)
    except TypeIdentification.DoesNotExist:
        return Response({'msn_client': 'El tipo de identificación ingresado no existe.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_type_identification(request):
    types_identification = TypeIdentification.objects.all()
    serializer = TypeIdentificationSerializer(types_identification, many=True)
    return Response(serializer.data)