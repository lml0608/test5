# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from django.http import HttpResponse

class MyException():

    def process_exception(request,response,exception):
        return HttpResponse(exception)
