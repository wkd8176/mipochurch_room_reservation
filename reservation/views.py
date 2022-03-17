from datetime import datetime, timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256

from .models import Reservation
from .forms import ReservationForm

# Create your views here.


class ReservationList(ListView):
    model = Reservation

    now = datetime.now()
    limit_date = now - timedelta(days=30)

    def get_context_data(self, **kwargs):
        context = super(ReservationList, self).get_context_data()

        return context

    def get_queryset(self):
        old_reservation = Reservation.objects.filter(end_time__lt=self.limit_date)
        if old_reservation:
            old_reservation.delete()
        return Reservation.objects.all()


def reservation_create(request):
    reservation = Reservation.objects.all()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            new_reservation = form.save(commit=False)
            password = form.cleaned_data.get('password')
            new_reservation.password = make_password(password)
            new_reservation.save()
            return redirect('reservation:main')
        else:
            error = form.errors.get_json_data(escape_html=True)
            error_message = error['__all__'][0]['message']
            messages.warning(request, error_message)
            return redirect('reservation:main')
    else:
        form = ReservationForm()
    context = {'reservation_list': reservation, 'form': form}
    return render(request, 'reservation/reservation_list.html', context)


def reservation_edit(request, pk):
    reservation_list = Reservation.objects.all()
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == "POST":
        form = ReservationForm(request.POST)
        form_password = request.POST['password']
        try:
            is_verified = django_pbkdf2_sha256.verify(form_password, reservation.password)
        except ValueError:
            messages.warning(request, '비밀번호가 맞지 않습니다.')
            return redirect('reservation:main')
        if is_verified:
            reservation.delete()
            if form.is_valid():
                edited_reservation = form.save(commit=False)
                edited_reservation.password = reservation.password
                edited_reservation.save()
                return redirect('reservation:main')
            else:
                error = form.errors.get_json_data(escape_html=True)
                error_message = error['__all__'][0]['message']
                messages.warning(request, error_message)
                reservation.save()
                return redirect('reservation:main')
        else:
            messages.warning(request, '비밀번호가 맞지 않습니다.')
            return redirect('reservation:main')
    else:
        form = ReservationForm(instance=reservation)
    context = {'reservation_list': reservation_list, 'form': form}
    return render(request, 'reservation/reservation_list.html', context)


def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == "POST":
        form_password = request.POST['password']
        try:
            is_verified = django_pbkdf2_sha256.verify(form_password, reservation.password)
        except ValueError:
            messages.warning(request, '비밀번호가 맞지 않습니다.')
            return redirect('reservation:main')
        if is_verified:
            reservation.delete()
            return redirect('reservation:main')
        else:
            messages.warning(request, '비밀번호가 맞지 않습니다.')
            return redirect('reservation:main')
    else:
        messages.warning(request, '비밀번호가 맞지 않습니다.')
        return redirect('reservation:main')
