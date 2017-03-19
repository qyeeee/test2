from django import forms


class ContactForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)
