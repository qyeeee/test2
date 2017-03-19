from django.contrib import auth
from django.core.mail import send_mail
from django.http import BadHeaderError
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from feedbackP.forms import ContactForm






def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():

            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']
            phone = form.cleaned_data['phone']

            recepients = ['my_email@ya.ru']

            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recepients.append(sender)


            try:
                send_mail(phone, message, 'my_email@ya.ru', recepients)

            except BadHeaderError: # Защита от уязвимости
                return HttpResponse('Invalid header found')

            return HttpResponseRedirect('/thanks.html')

    else:
        form = ContactForm()


    return render(reguest, 'feedback/contact.html', {'form': form, 'username': auth.get_user(reguest).username})


def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'feedback/thanks.html', {'thanks': thanks})

def base(request):
    return render(request, 'feedback/base.html')

'''Модель с файлом
def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST, request.FILES) <-----ошибка здесь(module 'django.http.request' has no attribute 'FILES')
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']


            recepients = ['my_email@ya.ru']





            if copy:
                recepients.append(sender)
            if 'file' in request.FILES:
                attach = request.FILES['file']

            try:
                send_mail(subject, message, 'my_email@ya.ru', recepients, attach)

            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('feedback/thanks.html')

    else:
        form = ContactForm()
    # Выводим форму в шаблон

    return render(reguest, 'feedback/contact.html', {'form': form, 'username': auth.get_user(reguest).username})'''

