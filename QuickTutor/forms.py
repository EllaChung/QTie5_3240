from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import QTUser, Review, Class, ClassNeedsHelp, Session, TutorableClass
#from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class ClassNeedsHelpForm(forms.ModelForm):
    class Meta:
        model = ClassNeedsHelp
        fields = ['class_id','elaboration']

class TutorableClassForm(forms.ModelForm):
    class Meta:
        model = TutorableClass
        fields = ['class_id','Former_TA', 'experience']

class CreateSessionForm(forms.ModelForm):
    start_date_and_time = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'],initial="M/D/Y Hour:Minute am/pm")
    end_date_and_time = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'],initial="M/D/Y Hour:Minute am/pm")

    class Meta:
        model = Session
        fields = ['tutor','subject_in_regards_to','price_of_tutor']
    
    def __init__(self, user, *args, **kwargs):
        super(CreateSessionForm, self).__init__(*args, **kwargs)
        class_possibilities_list = []
        tutor_possibilities_list = []

        for c in ClassNeedsHelp.objects.filter(user=user).values_list('class_id'):
            class_possibilities_list.append(c[0])

        for c in TutorableClass.objects.filter(user=user).values_list('class_id'):
            class_possibilities_list.append(c[0])
        
        for t in Session.objects.filter(student=user).filter(tutor_proposal='2').values_list('tutor'):
            tutor_possibilities_list.append(t[0])
        
        self.fields['subject_in_regards_to'].queryset = Class.objects.filter(id__in=class_possibilities_list)
        self.fields['tutor'].queryset = QTUser.objects.filter(pk__in = tutor_possibilities_list)


class CreateSpecificSessionForm(forms.ModelForm):
    start_date_and_time = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'],initial="M/D/Y Hour:Minute am/pm")
    end_date_and_time = forms.DateTimeField(input_formats=['%m/%d/%Y %I:%M %p'],initial="M/D/Y Hour:Minute am/pm")
    class Meta:
        model = Session
        fields = ['subject_in_regards_to','price_of_tutor']

    def __init__(self, tutor_id, *args, **kwargs):
        super(CreateSpecificSessionForm, self).__init__(*args, **kwargs)
        possibilities_list = []

        for c in TutorableClass.objects.filter(user=tutor_id).values_list('class_id'):
            possibilities_list.append(c[0])
        
        print(possibilities_list)
        self.fields['subject_in_regards_to'].queryset = Class.objects.filter(id__in=possibilities_list)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Recipient','subject_in_regards_to','rating','description','type_of_review']
    
    def __init__(self, user, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        class_possibilities_list = []
        review_possibilities_list = []

        for c in ClassNeedsHelp.objects.filter(user=user).values_list('class_id'):
            class_possibilities_list.append(c[0])

        for c in TutorableClass.objects.filter(user=user).values_list('class_id'):
            class_possibilities_list.append(c[0])
        
        self.fields['subject_in_regards_to'].queryset = Class.objects.filter(id__in=class_possibilities_list)

        for t in Session.objects.filter(student = user).filter(tutor_proposal='2').values_list('tutor'):
            review_possibilities_list.append(t[0])

        for s in Session.objects.filter(tutor = user).filter(student_proposal='2').values_list('student'):
            review_possibilities_list.append(s[0])
        
        self.fields['Recipient'].queryset = QTUser.objects.filter(pk__in=review_possibilities_list)


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = QTUser
        fields = ['first_name','last_name','year','rough_payment_per_hour','rough_willing_to_pay_per_hour']

'''
class MyForm(forms.Form):
    date_field = forms.DateField(widget=DatePicker())
    date_field_required_with_min_max_date = forms.DateField(
        required=True,
        widget=DatePicker(
            options={
                'minDate': '2009-01-20',
                'maxDate': '2017-01-20',
            },
        ),
        initial='2013-01-01',
    )
    """
    In this example, the date portion of `defaultDate` is irrelevant;
    only the time portion is used. The reason for this is that it has
    to be passed in a valid MomentJS format. This will default the time
    to be 14:56:00 (or 2:56pm).
    """
    time_field = forms.TimeField(
        widget=TimePicker(
            options={
                'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
                'defaultDate': '1970-01-01T14:56:00'
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ),
    )
    datetime_field = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )
'''