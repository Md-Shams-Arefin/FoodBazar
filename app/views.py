from django.shortcuts import render, redirect

from .models import *


def index(request):
    return render(request, 'app/index.html')


def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        people = request.POST.get('people')
        message = request.POST.get('message')

        book_a_table = Book_a_table(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            people=people,
            message=message
        )

        book_a_table.save()
        return redirect('index')
    return render(request, 'app/index.html')

def messageing(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message = Message(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        message.save()
        return redirect('index')
    return render(request, 'app/index.html')
