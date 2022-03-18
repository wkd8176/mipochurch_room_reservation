import re
from datetime import datetime, timedelta

from django import forms
from django.core.exceptions import ValidationError
from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['booker', 'participants', 'start_time', 'end_time', 'description', 'password']
        labels = {
            'booker': '예약자',
            'participants': '참석자',
            'start_time': '시작시간',
            'end_time': '종료시간',
            'description': '용도',
            'password': '비밀번호',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):

        now = datetime.now()

        cleaned_data = super().clean()

        cleaned_start = cleaned_data.get('start_time')
        cleaned_end = cleaned_data.get('end_time')

        cleaned_booker = cleaned_data.get('booker')
        cleaned_password = cleaned_data.get('password')

        reservations = Reservation.objects.all()

        start = "06:00"
        end = "22:00"
        reservation_start = datetime.strptime(start, '%H:%M')
        reservation_end = datetime.strptime(end, '%H:%M')

        if cleaned_booker is None:
            raise ValidationError('예약자 이름을 입력하세요')

        if cleaned_start is not None and cleaned_end is not None:

            if cleaned_start > cleaned_end:
                raise ValidationError('종료시간이 시작시간보다 과거일 수 없습니다.')

            if now > cleaned_start + timedelta(minutes=10):
                raise ValidationError('과거에 예약할 수 없습니다.')

            cleaned_start_date = cleaned_start.date()
            cleaned_end_date = cleaned_end.date()
            cleaned_start_time = cleaned_start.time()
            cleaned_end_time = cleaned_end.time()

            if cleaned_start_date != cleaned_end_date:
                raise ValidationError('하루 이상 예약할 수 없습니다.')

            if cleaned_start_time < reservation_start.time():
                raise ValidationError('오전 6시 이전에는 이용할 수 없습니다.')

            if cleaned_end_time > reservation_end.time():
                raise ValidationError('오후 10시 이후에는 이용할 수 없습니다.')

            if reservations.filter(
                    start_time__gt=cleaned_start, start_time__lt=cleaned_end).count() != 0 or reservations.filter(
                    end_time__gt=cleaned_start, end_time__lt=cleaned_end).count() != 0 or reservations.filter(
                    start_time__lte=cleaned_start, end_time__gte=cleaned_end).count() != 0:
                raise ValidationError('해당시간에 이미 예약이 있습니다.')

        elif cleaned_start is None and cleaned_end is not None:
            raise ValidationError('시작시간을 입력하세요')

        elif cleaned_start is not None and cleaned_end is None:
            raise ValidationError('종료시간을 입력하세요')

        else:
            raise ValidationError('시작시간과 종료시간을 입력하세요')

        if cleaned_password is None:
            raise ValidationError('비밀번호를 입력하세요')
        else:
            self.passwordValidation(cleaned_password)

    def passwordValidation(self, password):

        if len(password) < 8:
            raise ValidationError('비밀번호는 최소 8자 이상이어야 합니다.')

        # elif re.search('[0-9]+', password) is None:
        #     raise ValidationError('비밀번호는 최소 1개 이상의 숫자가 포함되어야 합니다.')

        # elif re.search('[a-zA-Z]+', password) is None:
        #     raise ValidationError('비밀번호는 최소 1개 영문 대소문자가 포함되어야 합니다.')

        # elif re.search('[`~!@#$%^&*<.>/?]+', password) is None:
        #     raise ValidationError('비밀번호는 최소 1개 이상의 특수문자가 포함되어야 합니다.')

        else:
            return True
