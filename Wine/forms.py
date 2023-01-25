from django import forms


class TextInputForm(forms.Form):
    input_text = forms.CharField(max_length=100)
