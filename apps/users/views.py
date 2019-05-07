import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponseRedirect

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm, UploadImageForm, UserInfoForm
from utils.email_send import send_register_email
from utils.mixin_utils import LoginRequireMixin
from .models import Banner
from paper.models import Type
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:

            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已存在！"})
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form": register_form})


class LoginView(View):

    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    all_banners = Banner.objects.all().order_by('index')
                    return render(request, "index.html", {
                        "all_banners": all_banners
                    })
                else:
                    return render(request, 'login.html', {"msg": "用户未激活！"})
            else:
                return render(request, 'login.html', {"msg": "用户名或密码错误！"})
        else:
            return render(request, 'login.html', {"login_form": login_form})


class ForgetPwdView(View):

    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgrtpwd.html", {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email')
            send_register_email(email, "forget")
            return render(request, "send_success.html")
        else:
            return render(request, "forgrtpwd.html", {"forget_form": forget_form})


class ResetView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email": email, "msg": "密码不一致！"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, "login.html")
        else:
            email = request.POST.get("email")
            return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})


class IndexView(View):

    def get(self, request):
        current_page = "home"
        all_banners = Banner.objects.all().order_by('index')
        # banner_type = Type.objects.filter(is_banner=True)[:4]
        return render(request, "index.html", {
            "all_banners": all_banners,
            # "banner_type": banner_type,
            "current_page": current_page
        })


class UserInfoView(LoginRequireMixin, View):

    def get(self, request):
        return render(request, 'usercenter-info.html', {})

    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status": "success", "msg":"修改成功"}', content_type="application/json")
        else:
            return HttpResponse(json.dump(user_info_form.errors), content_type="application/json")


class UploadImageView(LoginRequireMixin, View):

    def post(self, request):
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            request.user.save()
            return HttpResponse('{"status": "success", "msg":"修改成功"}', content_type="application/json")
        else:
            return HttpResponse('{"status": "fail", "msg":"修改失败"}', content_type="application/json")


class UpdatePwdView(View):

    def post(self,request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1 != pwd2:
                return HttpResponse('{"status": "fail", "msg":"修改失败"}', content_type="application/json")
            user = request.user
            user.password = make_password(pwd2)
            user.save()
            return HttpResponse('{"status": "success", "msg":"修改成功"}', content_type="application/json")
        else:
            return HttpResponse(json.dump(modify_form.errors), content_type="application/json")




