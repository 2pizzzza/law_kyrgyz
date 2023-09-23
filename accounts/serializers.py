from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email',
                  'middle_name', 'phone_number', 'password',
                  'gender', 'citizenship', 'date_of_birth',
                  'document_id', 'date_of_expiry', 'place_of_birth',
                  'authority', 'date_of_issue', 'ethnicity', "personal_number"
                  ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data['middle_name'],
            phone_number=validated_data['phone_number'],
            gender=validated_data['gender'],
            citizenship=validated_data['citizenship'],
            date_of_birth=validated_data['date_of_birth'],
            date_of_expiry=validated_data['date_of_expiry'],
            document_id=validated_data['document_id'],
            authority=validated_data['authority'],
            date_of_issue=validated_data['date_of_issue'],
            ethnicity=validated_data['ethnicity'],
            personal_number=validated_data['personal_number'],
            place_of_birth=validated_data['place_of_birth'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
