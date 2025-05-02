from django import forms
from .models import Tournament


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'description', 'category', 'num_participants', 'match_type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'match_type': forms.Select(attrs={'class': 'form-control'}),
        }

class JoinTournamentForm(forms.Form):
    code = forms.CharField(max_length=20, label="Tournament Code", widget=forms.TextInput(attrs={'class': 'form-control'}))