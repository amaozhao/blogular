# coding: utf-8
'''
Created on 2014年12月31日

@author: amaozhao
'''
from django.views.generic.base import View
from django.http import JsonResponse
from django.utils.translation import ugettext as _

from api.serializers.user import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from django.contrib.auth import logout, login, authenticate
from rest_framework.response import Response


class AuthUserView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

    def get_object(self):
        if self.request.user.is_authenticated():
            return self.request.user
        return None

    def retrieve(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({})


class SignInView(View):

    def get(self, request, *args, **kwargs):
        return Response({}, status=400)

    def post(self, request, *args, **kwargs):
        import json
        obj = json.loads(request.body)
        username = obj['username']
        password = obj['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                json_user = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'is_active': user.is_active
                }
                message = {'status': 200, 'user': json_user}
                return JsonResponse(message)
            else:
                message = {
                    'status': 403,
                    'message': _('This user is inactived. Please active!')
                }
                return JsonResponse(message, status=403)
        else:
            message = {
                'status': 403,
                'message': _(
                    'This user is not registered. Please register first!')
            }
            print 110
            return JsonResponse(message, status=403)


class SignOutView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        logout(self.request)
        return Response({'message': 'success'}, status=200)
