from django import forms
from .models import Tournament, Player


class TournamentForm(forms.ModelForm):
    players = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter player names, one per line',
            'rows': 5,
            'class': 'w-full p-2 rounded bg-gray-800 text-white border border-gray-600 focus:ring-2 focus:ring-orange-500'
        }),
        required=True,
        label="Players"
    )

    class Meta:
        model = Tournament
        fields = ['name', 'description', 'category', 'num_participants', 'match_type']
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-2 rounded bg-gray-800 text-white border border-gray-600 focus:ring-2 focus:ring-orange-500'
            }),
            'match_type': forms.Select(attrs={
                'class': 'w-full p-2 rounded bg-gray-800 text-white border border-gray-600 focus:ring-2 focus:ring-orange-500'
            }),
        }

class JoinTournamentForm(forms.Form):
    code = forms.CharField(max_length=20, label="Tournament Code", widget=forms.TextInput(attrs={'class': 'form-control'}))

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'team_name']  # Include team_name