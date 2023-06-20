# 1-导包
from loguru import logger
from settings import retention, rotation, log_name
from unittestreport import TestRunner
import unittestreport
from settings import testcase_dir, testreport_dir, testlog_dir
import unittest
import requests
# """
# 1- 先登录
# 2-带上token调图片上传接口:
#     后台-图片上传接口：http://mall.lemonban.com:8108/admin/file/upload/img
#     请求方法：post
#     请求头 headers中：
#     Content-Type：multipart/form-data
#     Authorization：bearer6ca911cd-4cee-42c0-8c72-b8503bcbf738
#     参数：resquests中files参数
# """
#
# import requests
# # 1- 登录操作
# url = "http://mall.lemonban.com:8108/adminLogin"
# json ={
#     "principal":"student",
#     "credentials":"123456a",
#     "imageCode":"lemon"
# }
# resp = requests.request("post",url,json=json)
# print(resp.json())
#
# # 提取'access_token'拼接 Authorization：bearer6ca911cd-4cee-42c0-8c72-b8503bcbf738
# url ="http://mall.lemonban.com:8108/admin/file/upload/img"
# header = {'Authorization':f'bearer{resp.json()["access_token"]}'}
# files = {"file":("code.png",open("code.png","rb"))}
# # print(files)
# resp = requests.request("post",url,files=files,headers=header)
# print(resp.text)


#
# url = "https://testbox.alphalawyer.cn/seafhttp/upload-api/0f241ae7-bc4d-476c-9e57-1cc1e88f8d10"
# payload={}
# method="post"
# files = {"file":("image1.jpeg",open("image1.jpeg","rb"))}
# headers = {
#   'authorization': 'Token 7e66b3e304c2e7e575b8fa61ffac1910fb6c8837',
#   'token': 'eyJhbGciOiJIUzI1NiJ9.eyJvZmZpY2VfaWQiOiIzMTRFRUUzREM4NzUxMUVEODY2NTBDNDJBMUI3QzUyNiIsImRldmljZVR5cGUiOiJ3ZWIiLCJvZmZpY2VfbmFtZSI6Iui0ouWKoeWIhumFjeS4k-eUqOW-i-aJgHRlc3QiLCJ1c2VyX3R5cGUiOiJBIiwidXNlcl9pZCI6IjMxNTNCNERDQzg3NTExRUQ4NjY1MEM0MkExQjdDNTI2IiwibG9naW5UeXBlIjoiMiIsInVzZXJfbmFtZSI6IuW8oOWAqSIsImlzcyI6ImlMYXcuY29tIiwiZXhwIjoxNjgyNjYxMjMwMzEwLCJpYXQiOjE2ODIwNTY0MzAzMTAsIm9mZmljZVR5cGUiOiJpbnRlZ3JhdGlvbiJ9.vJH0p9h-voA_Z9PbfyXRQqisTqSCjGwDa3ZyofHVdlI'
# }
# json = {"parent_dir":"/","relative_path":""}
# response = requests.request("POST", url, headers=headers,data=json, files=files)
# print(response)