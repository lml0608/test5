from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
import os
from .models import *
from django.core.paginator import *
import json
# Create your views here.

def index(request):

    return render(request,'booktest/index.html')

def MyExp(request):
    a1 = int('abc')
    return HttpResponse("hello")

def uploadPic(request):

    return render(request,'booktest/uploadPic.html')

def uploadHandle(request):

    pic1 = request.FILES['pic1']

    fname = '%s/cars/%s' % (settings.MEDIA_ROOT,pic1.name)
    picName = os.path.join(settings.MEDIA_ROOT,pic1.name)
    print(settings.MEDIA_ROOT)
    with open(picName,'wb+') as pic:
        for c in pic1.chunks():
            pic.write(c)

    return HttpResponse('<img src="/static/media/%s" />' % pic1.name)


#分页练习
def herolist(request,pindex):
    #判断pindex是否为空
    if pindex == '':
        pindex = '1'
    herolist = HeroInfo.objects.all()

    paginator = Paginator(herolist,5)
    page = paginator.page(int(pindex))

    context = {'page':page}

    return render(request,'booktest/herolist.html',context)

#省市区选择
def area(request):

    #areaDate = Areas.objects.get(pk=130100)

    return render(request,'booktest/area.html')

def area2(request,id):
    id1 = int(id)

    if id1 == 0:
        data = AreaInfo.objects.filter(parea__isnull=True)
    else:
        data =[{}]

    # list = []
    for area in data:
        list.append(area)
    data1 = {'data':data}
    data2 = json.dumps(data1)
    return JsonResponse(data2)
