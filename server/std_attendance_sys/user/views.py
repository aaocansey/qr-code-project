from io import BytesIO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from user.api.serializer import LecturerSerializer, StudentSerializer, LoginLecturerSerializer, ListLecturersSerializer, QRSerializer
from user.models import User, Lecturer, Student 

from user.api.utils import generate_qr
from rest_framework.decorators import action

from django.contrib.auth import authenticate, login


class CreateStudentView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_data = serializer.validated_data
        
        user = User.objects.create_user(**user_data)
        user.save()
        
        student = Student.objects.create(user=user)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LecturerCreateView(APIView):
    
    def post(self, request):
        serializer = LecturerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract user data from validated data
        user_data = serializer.validated_data

        # Extract password assuming it's sent in request.data (adjust based on your setup)
        password = request.data.get('password')
        if not password:
            raise serializer.ValidationError('Password is required.')

        # Create User object with password setting
        user = User.objects.create_user(username=user_data['email'], email=user_data['email'])
        user.set_password(password)
        user.save()
        
        lecturer = Lecturer.objects.create(user=user)
        serializer = LecturerSerializer(lecturer) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class LecturerLoginView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = LoginLecturerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(email=email, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=400)

        login(request, user)
        # token, _ = Token.objects.get_or_create(user=user)
        return Response(email, status= status.HTTP_200_OK)
        

class LecturerQRCodeView(APIView):
  def post(self, request):
    data_to_encode = request.data  # Customize as needed

    try:
      qr_code = generate_qr(data_to_encode)  # Assuming you're using pyqrcode
      output = generate_qr(qr_code)
      result = QRSerializer(output).data
      return Response(
            data=result,
            status=status.HTTP_201_CREATED
        )

    except Exception as e:
      # Handle exception (e.g., log the error and return a 500 Internal Server Error)
      return Response({'error': 'Failed to generate QR code'}, status=500)       


class ListLecturersView(APIView):
    
    def get(self, request):
        queryset = Lecturer.objects.all()
        serializer = ListLecturersSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        
        
    
    
    
    
    
# # alternatively
# user = User()  # Create a blank user object
# user.username = user_data['username']
# user.email = user_data['email']
# user.set_password(password)
# user.save()  # Save the user with the hashed password