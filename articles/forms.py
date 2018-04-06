from django import forms

LIST_CHOICES= [
    ('antiguos primeros', 'Más antiguos: primeros'),
    ('antiguos últimos', 'Más antiguos: últimos'),
    ]

class ListTypeForm(forms.Form):
    list = forms.Charfield(widget=forms.Select(choices=LIST_CHOICES))