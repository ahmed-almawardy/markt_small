from django.urls import conf
from rest_framework import serializers
from rest_framework.exceptions import APIException
from user.models import User
from user.validators import password_validator

#TODO::Refactor remove Dupicate code
class UserPasswordUpdate(serializers.ModelSerializer):
    confirm_password = serializers.CharField( max_length=150, style={"input_type":'password'}, write_only=True)
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'confirm_password',
            )
        extra_kwargs = {
            'confirm_password': {'write_only': True}
        }
        
    def create(self, validated_data):
        raise NotImplementedError()
    
    def update(self, instance, validated_data):
        self.update_password_if_exists(validated_data)
        return super().update(instance, validated_data)

    def password_validate(self, password):
        
        '''
        preforming a validationg phase
        '''
        password_validator.validate(password)

    def is_password_match(self, validated_data, raise_execption):
        
        '''
        for password matching availability
        '''
        matched = validated_data['password'] == validated_data.pop('confirm_password')
        if not matched and raise_execption:
            raise APIException('passwords don\'t match')
        return matched

    def update_password_if_exists(self, validated_data):
        self.is_password_exited(validated_data)
        self.is_password_match(validated_data, raise_execption=True)
        self.password_validate(validated_data['password'])
        self.instance.set_password(validated_data.pop('password'))
        self.instance.save()

    def is_password_exited(self, validated_data):
        password = validated_data.get('password')
        confirm_password = validated_data.get('confirm_password', None)
        return (not password is None) and  (not confirm_password is None)


class UserSerializerCreate(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, max_length=150, style={"input_type":'password'}, write_only=True)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'confirm_password'
        )
        extra_kwargs = {
            'password': 
            {
                'style': {"input_type": 'password'},
            }
        }

    def create(self, validated_data):
        passed_password = validated_data.pop('confirm_password')
        self.is_password_match(passed_password, raise_execption=True)
        self.password_validate(validated_data['password'])

        return self.Meta.model.create(validated_data)

    def password_validate(self, password):
        
        '''
        preforming a validationg phase
        '''
        password_validator.validate(password)

    def is_password_match(self, passed_password,raise_execption):
        
        '''
        for password matching availability
        '''
        matched = self.validated_data['password'] == passed_password
        if not matched and raise_execption:
            raise APIException('passwords don\'t match')
        return matched


class UserSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            # 'token',
            'email'
        )

