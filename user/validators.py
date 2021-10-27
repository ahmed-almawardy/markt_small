from django.contrib.auth.password_validation import (UserAttributeSimilarityValidator, MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator)

from rest_framework.exceptions import APIException


class Password:
    '''
    class for validate a password
    '''

    def __init__(self, validators_add=None) -> None:
        self.validators = [
            UserAttributeSimilarityValidator,
            MinimumLengthValidator,
            CommonPasswordValidator,
            NumericPasswordValidator
        ]
 
        if validators_add:
            self.validators.extend(validators_add)


    def validate(self, password):
        try:
            for validator in self.validators:
                validator().validate(password=password)
        except Exception as e:
            raise APIException(f'password error:{str(e)}')
 

password_validator = Password()