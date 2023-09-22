from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name' : TextInput(attrs={'class' : 'input', 'placeholder': '도시를 입력하세요.'}),
        }
        
    def clean_name(self):
        name = self.cleaned_data['name']
        if City.objects.filter(name=name).exists():
            raise forms.ValidationError('이미 존재하는 도시입니다.')
        return name