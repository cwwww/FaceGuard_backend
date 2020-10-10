from django.shortcuts import render
import os
import base64
# Create your views here.
from rest_framework.mixins import Response
from rest_framework.views import APIView
from .models import User



current_path = os.path.dirname(__file__)

def response_success_200(res={}):
    """
    返回请求成功
    :param data_dict:
    :return: response(dict)
    """
    response = dict()
    response['msg'] = '请求成功'
    response['result'] = res
    response['code'] = 200
    return Response(response, status=200)


def response_failed_400():
    """
    返回请求失败
    :return: response(dict)
    """
    response = dict()
    response['msg'] = '请求参数错误'
    response['result'] = dict()
    response['code'] = 400
    return Response(response, status=400)



class SaveUserInfo(APIView):
    def post(self, request):
        response = {}
        try:
            data = request.data
            print(data)
            img_data = base64.b64decode(data["img"])

            new_user = User(name=request.data['name'],address=request.data['address'],sex= request.data['sex'],
                            age=request.data['age'],job=request.data['job'])
            new_user.save()
            img_url = './images/' + str(new_user.user_id) + '.jpg'

            with open(img_url, 'wb') as f:
                f.write(img_data)

        except  Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
            print(str(e))
        return Response(response, status=200)
