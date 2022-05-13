from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from .models import ArmyShop, Course

def course_ajax(request):
    return render(
        request, 'secondapp/course_ajax.html', {})
    #jeju_olle_list = JejuOlle.objects.all()

def req_get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET['c']
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)
def req_ajax4(request):
    return render(request, 'firstapp/ajax4.html')


def army_shop2(request, year, month):
    shops = ArmyShop.objects.filter(year=year,month=month)
    # result = ''
    # for c in curriculum:
    # result += c.name + '<br>'
    # return HttpResponse(result)
    return render(request, 'secondapp/army_shop.html', {
        'data': shops
    })


def army_shop(request):
    # shops = ArmyShop.objects.all()
    # result = ''
    # for c in curriculum:
    # result += c.name + '<br>'
    # return HttpResponse(result)
    #             GET['prd']
    prd = request.GET.get('prd')
    if not prd: #prd에 값이 없을 경우
        prd =''
    shops = ArmyShop.objects.filter(name__=prd)
    return render(request, 'secondapp/army_shop.html', {
        'data': shops
    })


def show(request):
    course = Course.objects.all()
    # result = ''
    # for c in curriculum:
    # result += c.name + '<br>'
    # return HttpResponse(result)
    return render(request, 'secondapp/show.html', {
        'data': course
    })

# def show(request):
#     course = Course.objects.all()
#     result = ''
#     for c in course:
#         result += c.name + '<br>'
#     return HttpResponse(result)


def insert(request):
    Course(name='데이터 분석',cnt=30).save()
    Course(name='데이터 수집',cnt=20).save()
    Course(name='웹개발',cnt=25).save()
    Course(name='인공지능',cnt=20).save()

    return HttpResponse('완료')

def main(request):
    return HttpResponse('<h1><u>Main</u></h1>')
