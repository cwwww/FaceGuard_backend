from django.shortcuts import render
import os
import base64
# Create your views here.
from rest_framework.mixins import Response
from rest_framework.views import APIView
from .models import User
from .cropFaces import crop


current_path = os.path.dirname(__file__)
img_path = './images/'
dlib_path = './model/shape_predictor_68_face_landmarks.dat'
crop_path = './images_crop/'
rectangle_path = './images_rectangle/'

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


class RegisterCheck(APIView):
    # check if the name already has been used, if yes return true
    def post(self,request):
        data = request.data
        name = data['name']
        try:
            exit_user = User.objects.get(name=name)
            res = {"user_exist": True}
        except:
            res = {"user_exist": False}

        print(res)
        return response_success_200(res)



class SaveUserInfo(APIView):
    # save the user's info into database
    def post(self, request):
        data = request.data
        print(data)
        img_data = base64.b64decode(data["img"])
        img_name = data["name"] + '.jpg'
        img_url = img_path + img_name  # original image save path
        with open(img_url, 'wb') as f:
            f.write(img_data)
        print(img_name)

        # detect whether this image contain a face, if yes save everything
        has_face = crop(img_path + img_name,crop_path, rectangle_path,dlib_path)
        print(has_face)
        img_path_database = crop_path + img_name  # cropped face path in database
        if has_face:
            new_user = User(name=request.data['name'],address=request.data['address'],sex= request.data['sex'],
                            age=request.data['age'],job=request.data['job'],image=img_path_database)
            new_user.save()

        res = {"has_face": has_face}
        return response_success_200(res)
