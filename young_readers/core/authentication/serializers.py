from rest_framework import serializers
from .models import Users, UserChilds



class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'profile_pic')
        

class UsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'first_name', 'email','last_name', 'mobile_no', 'address')

class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile_no', 'address')


class UserChildsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserChilds

class UsersDtlSerializer(serializers.ModelSerializer):
    childs = UserChildsSerializer(many = True, read_only = True)
    
    class Meta:
        model = Users
        fields = ('username','first_name','last_name','email','is_superuser','date_joined','date_of_birth','premium_user','subscription_date','noti_count','profile_pic','mobile_no','mobile_verified','subscription_type','books_hold','address','auth_thru', 'childs')