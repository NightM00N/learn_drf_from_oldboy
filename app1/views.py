from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import json

# Create your views here.

class OrderView(View):
    def get(self, request, *args, **kwargs):
        ret = {
            'code':1000,
            'msg':"ajsnb"
        }
        return HttpResponse(json.dumps(ret))

    def post(self, request, *args, **kwargs):
        return HttpResponse('post')

    def put(self, request, *args, **kwargs):
        return HttpResponse('put')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('delete')



from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions
from rest_framework.request import Request

class MyAuthentication(object):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return ('zjm', None)

    def authenticate_header(self, val):
        pass


class DogView(APIView):
    # 覆盖APIView中的DEFAULT_AUTHENTICATION_CLASSES，里面是BasicAuthentication对象
    authentication_classes = [MyAuthentication, ]

    def get(self, request, *args, **kwargs):
        self.dispatch
        print(request)
        print(request.user)
        ret = {
            'code': 1000,
            'msg': "ajsnb"
        }
        return HttpResponse(json.dumps(ret))

    def post(self, request, *args, **kwargs):
        return HttpResponse('post')

    def put(self, request, *args, **kwargs):
        return HttpResponse('put')

    def delete(self, request, *args, **kwargs):
        return HttpResponse('delete')
