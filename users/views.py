from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
import jwt, datetime
from .models import User
import os

class RegisterView(APIView):
  
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
class LoginView(APIView):
  def post(self, request):
    email = request.data['email']
    password = request.data['password']
    
    user = User.objects.filter(email=email).first()
    
    if user is None:
      raise AuthenticationFailed('User not found')
    
    if not user.check_password(password):
      raise AuthenticationFailed('Incorrect password')
    
    payload = {
      'id': user.id,
      'iat': datetime.datetime.utcnow(),
      'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
    }
    
    auth_secret = os.getenv('AUTH_SECRET')
    token = jwt.encode(payload, auth_secret, 'HS256')
    
    response = Response()
    response.data = { 'token': token }
    response.set_cookie(key='jwt_token', value=token, httponly=True, secure=True)
    
    return response
  
class UserView(APIView):
  def get(self, request):
    token = request.COOKIES.get('jwt_token')
    
    if not token:
      raise AuthenticationFailed('Unauthorized')
    
    auth_secret = os.getenv('AUTH_SECRET')
    
    try:
      payload = jwt.decode(token, auth_secret, ['HS256'])
    except jwt.ExpiredSignatureError:
      raise AuthenticationFailed('Token expired')
    
    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)
    
    return Response(serializer.data)
  
class LogoutView(APIView):
  def post(self, request):
    response = Response()
    response.delete_cookie('jwt_token')
    response.data = {
      'message': 'Logged out'
    }

    return response
    
      
    
    