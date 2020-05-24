from django import forms

class too(forms.Form):
    task = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control",'placeholder':'Enter your task here'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control','placeholder':'Enter Description of your task','rows':'4'}))
