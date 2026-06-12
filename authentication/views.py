from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import LoginForm, CustomUserCreationForm

def login_view(request):
    make_redirect(request, form_class=LoginForm)
    form = restore_session(request, form_class=LoginForm)
    return render(request, 'login.html', {'form': form})

def register(request):
    make_redirect(request, form_class=CustomUserCreationForm)
    form = restore_session(request, form_class=CustomUserCreationForm)
    return render(request, 'register.html', {'form': form})


def make_redirect(request, form_class):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            user = form.save() if hasattr(form, 'save') else form.get_user()
            login(request, user)
            messages.success(request, "Ви успішно зареєструвалися!")
            request.session.pop('form_data', None)  # Очистка збережених даних
            request.session.pop('form_errors', None)  # Очистка помилок
            return redirect('home')

        request.session['form_data'] = request.POST.dict()
        request.session['form_errors'] = form.errors.get_json_data()
        return redirect(request.path)

def restore_session(request, form_class):
    form_data = request.session.pop('form_data', None)
    form_errors = request.session.pop('form_errors', None)

    form = form_class(data=form_data)
    if form_errors:
        # Повністю замінюємо помилки форми
        form._errors = {}  # Очищення попередніх помилок
        for field, errors in form_errors.items():
            form._errors[field] = [error['message'] for error in errors]
    return form
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout



