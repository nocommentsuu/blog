from django.shortcuts import render, redirect
from core.auth_models import User
from django.contrib.auth import login, logout, authenticate

def register(request):
    errors = {}
    ctx = {}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("confirm")

        # Проверка пустых полей
        if not username:
            errors["username"] = "Username kiritilishi kerak"
        if not password:
            errors["password"] = "Parol kiritilishi kerak"
        if not password_confirm:
            errors["confirm"] = "Tasdiqlash paroli kiritilishi kerak"

        # Username занят?
        if username and User.objects.filter(username=username).exists():
            errors["username"] = "Bu username band"

        # Пароли не совпадают
        if password and password_confirm and password != password_confirm:
            errors["confirm"] = "Parollar mos emas"
        print("error bor >>>>", errors)
        # Если ошибок нет — создаём пользователя + логиним
        if not errors:
            user = User.objects.create_user(
                username=username,
                password=password
            )

            # 🔥 Автоматический вход
            login(request, user)
            authenticate(request)

            # Редирект домой
            return redirect("home")

    ctx["errors"] = errors
    return render(request, "partials/register.html", ctx)



def loginn(request):
    errors = {}

    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")

        if not name:
            errors["username"] = "Username kiritilishi kerak"
        if not password:
            errors["password"] = "Parol kiritilishi kerak"

        if not errors:
            user = User.objects.filter(username=name).first()
            if not user:
                errors["username"] = "Bunday foydalanuvchi mavjud emas"
            elif not user.check_password(password):
                errors["password"] = "Parol noto‘g‘ri"
            else:
                login(request, user)
                return redirect("home")

    return render(request, "partials/login.html", {"errors": errors})


def logoutt(request):
    if request.method == "POST":
        logout(request)
    return redirect("home")
