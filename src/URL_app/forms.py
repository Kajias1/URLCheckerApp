from django import forms
from .models import URLRecord

class URLRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = URLRecord
        fields = ['url']
        widgets = {
            'url': forms.URLInput(attrs={
                'class':'form-control mr-sm-2', 'type':'search', 'placeholder': 'Ссылка в виде URL', 'aria-label':'Search'
                })
        }