from django.contrib.auth.forms import UserCreationForm
from .models import ShopUser


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = (
            #'username', #from AbstractUser
            'first_name', #from AbstractUser
            'last_name', #from AbstractUser
            'email', #from AbstractUser
            'password1',
            'password2',
            'nickname' #from ShopUser переоп. Username
            'age', #from ShopUser
            'avatar' #from ShopUser
        )

# стилизация элементов формы
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'form-control'
        field.help_text = ''

# проверка возраста пользователя
def check_age(self):
    data = delf.cleaned_data['age']
    if data < 12:
        raise forms.ValidationError('Сайт предназначен для пользователей старше 12 лет')
    return data