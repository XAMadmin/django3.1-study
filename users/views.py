from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
import json
from django.views.generic import View
from users.forms import IssueForm
from users.models import Issue
from django.contrib import messages

# Create your views here.

def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    context = {'username':'张三'}
    # return HttpResponse('Hello There~')
    return render(request, 'index.html', context)


def say(request):

    
    url = reverse('users:index')  # 返回 /users/index/
    print(url)
    # return HttpResponse('say')
    # return JsonResponse({'city': 'wuhan', 'subject': 'python'})
    return redirect('users:index')


def birthday(request, year, month):
    print(year)
    print(month)

    return HttpResponse('OK')


def sending_get(request):
    name = request.GET.get("name")
    print(name)

    return HttpResponse("我的名称：" + name)


def sending_post(request):
    name = request.POST.get("name")
    print(name)

    return HttpResponse("我的名称：" + name)


def sends_json(request):
    json_str = request.body
    data = json.loads(json_str)
    print(data)
    return HttpResponse("OK")


def set_cookies(request):
    response = HttpResponse('OK,设置cookie')

    response.set_cookie('user_id', '1', max_age=3600)

    return response


def get_cookies(request):
    user_id = request.COOKIES.get("user_id")
    return HttpResponse("user_id:" + user_id)


def set_session(request):
    request.session["session_id"] = '2'
    print(request.session.get("session_id"))
    return HttpResponse("session_id:" + request.session.get("session_id"))



def checking(request):

    if request.method == 'GET':

        return render(request, 'register.html')
    
    else:

        return HttpResponse("业务注册逻辑")
        


# 定义类视图
class Checking(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        return HttpResponse("业务注册逻辑")


class AddView(View):
    def get(self, request):
        form = IssueForm()
        return render(request, 'issues/add.html', {'form':form})
    
    def post(self, request):
        form = IssueForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            print(request.user.id)
            try:
                issue = Issue.objects.create(user_id=request.user.id, title=title, content=content)
                messages.success(request, "新增成功！")
                return HttpResponseRedirect(reverse('users:detail'))
            except Exception as e:
                print(e)
                messages.error(request, "数据库存储异常！缺少参数值" )
                return redirect("users:addview")

           
            # return redirect(reverse('users:detail'))
        else:
            return render(request, 'issues/add.html', {'form': form})


def detail(request):
    # id = request.args
    # print(id)
    return render(request, 'issues/detail.html')
             