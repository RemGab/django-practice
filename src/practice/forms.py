from django import forms
from store.models import Booking


JOBS = (
    ("python", "Developpeur Python"),
    ("javascript", "Developpeur javascript"),
    ("csharp", "Developpeur csharp"),
    
)

class SignupForm (forms.Form):
    pseudo = forms.CharField(max_length=8,required=False,strip=True)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect())
    cgu_accept = forms.BooleanField(initial=True)
    
    def clean_pseudo(self):
        pseudo = self.cleaned_data.get('pseudo')
        if '$' in pseudo :
            raise forms.ValidationError("Le pseudo non")
        return pseudo
    
class Blop(forms.ModelForm):
    class Meta : 
        model = Booking
        fields = [
            "title",
            "auteur",
            'slug',
            'content'
        ]
        
        labels = { 'title' : 'Titre'}