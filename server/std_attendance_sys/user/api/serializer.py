from rest_framework import serializers
from user.models import Student, Lecturer, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'phone_number')  # Include desired user details
        # Set source for fields coming from the User model
        extra_kwargs = {
            'name': {'source': 'user.first_name'},
            'phone_number': {'source': 'user.phone_number'},
        }

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ('user', 'index_num', 'course',)


class LecturerSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField()
    
    class Meta:
        model = Lecturer
        fields = ('email',)
        

class ListLecturersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lecturer
        fields = ('user', 'email')        
        
class LoginLecturerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lecturer
        fields = ('email', 'password')    
        
        



class QRSerializer(serializers.Serializer):
    """
    This serializer is the output of create qr code
    """
    file_type = serializers.CharField(max_length=5)
    image_base64 = serializers.CharField(max_length=300)    
        
    