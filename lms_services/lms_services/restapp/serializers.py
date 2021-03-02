from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework import serializers
from .models import Student,Faculty,Category,Course,Course_Session,Enrolled_Session
class GroupSerializer(serializers.ModelSerializer):
    #students = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    #faculties = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = Group
        #fields = ['id','name','students','faculties']
        fields = ['id','name']

class UserSerializer(serializers.ModelSerializer):
    courses_created = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())
    courses_taken = serializers.PrimaryKeyRelatedField(many=True, queryset=Course_Session.objects.all())
    courses_enrolled = serializers.PrimaryKeyRelatedField(many=True, queryset=Enrolled_Session.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'groups','courses_created','courses_taken','courses_enrolled'] 

class StudentSerializer(serializers.ModelSerializer):
    #user_group = serializers.ReadOnlyField(source = 'user.groups',many=True,read_only=True,)
    #user_firstname = serializers.ReadOnlyField(source = 'user.first_name')
    #user_lastname = serializers.ReadOnlyField(source = 'user.last_name')
    #user_email = serializers.ReadOnlyField(source = 'user.email')
    
    class Meta:
        model = Student
        #fields = ['id','user_firstname','user_lastname','user_email','dob', 'education', 'address', 'city', 'pin', 'phone1','phone2']
        #fields = ['id','name','group','password','dob',  'address', 'city', 'pin', 'email','phone']
        fields = ['id','name','password','dob',  'address', 'city', 'pin', 'email','phone']

        #extra_kwargs = {'password': {'write_only': True}}
class FacultySerializer(serializers.ModelSerializer):
    #user_group = serializers.ReadOnlyField(source = 'user.groups',many=True,read_only=True,)
    #user_firstname = serializers.ReadOnlyField(source = 'user.first_name')
    #user_lastname = serializers.ReadOnlyField(source = 'user.last_name')
    #user_email = serializers.ReadOnlyField(source = 'user.email')
    
    class Meta:
        model = Faculty
        #fields = ['id','user_firstname','user_lastname','user_email','dob', 'education', 'address', 'city', 'pin', 'phone1','phone2']
        #fields = ['id','name','group','password','dob',  'address', 'city', 'pin', 'email','phone']
        fields = ['id','name','password','dob',  'address', 'city', 'pin', 'email','phone']
        #extra_kwargs = {'password': {'write_only': True}}
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')
class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Course
        fields = ('id','category','name','credit','duration','owner')
class CourseSessionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Course_Session
        fields = ('id','course','taken_by','tot_seats','rem_seats','start_date','end_date','owner')
class EnrolledSessionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Enrolled_Session
        fields = ('id','enrolled_by','course','owner')
                 