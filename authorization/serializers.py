from rest_framework import serializers
from authorization.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
 
    date_joined = serializers.ReadOnlyField()
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    
    class Meta(object):
        model = User
        fields = ('email', 'first_name', 'token', 'last_name',
                  'password','date_joined')
    

    def get_token(self, user):
        refresh_token = RefreshToken.for_user(user)
        return{
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance