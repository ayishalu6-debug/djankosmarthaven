from django.shortcuts import render

from smarthavenapp.serilaisers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class userregistrationapi(APIView):
    def post(self,request):
        user_serial=usertableserializers(data=request.data)
        login_serial=logintableseriliazers(data=request.data)
        data_valid=user_serial.is_valid()
        login_valid=login_serial.is_valid()
        if data_valid and login_valid:
            login_profile=login_serial.save(usertype='user')
            user_serial.save(LOGIN_ID=login_profile)
            return Response(user_serial.data,status=status.HTTP_201_CREATED)
        return Response({'loginerror':login_serial.errors if not login_valid else None,'usererror':user_serial.errors if not data_valid else None},status=status.HTTP_400_BAD_REQUEST)