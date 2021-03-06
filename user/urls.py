from django.urls import path
from user.view import *

app_name = 'user'

urlpatterns = [
    path('register', user_register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('codelogin', code_login, name='codelogin'),
    path('send_code', send_code, name='send_code'),
    path('forget_pwd', forget_password, name='forget_pwd'),
    path('valide_code', valide_code, name='valide_code'),
    path('update_pwd', update_pwd, name='update_pwd'),
    path('center', user_center, name='center'),
    path('center1', user_center1, name='center1'),
    path('zhuce', user_zhuce, name='zhuce'),
    path('manager', user_manager, name='manager')

]
