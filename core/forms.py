from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=255)
    email = forms.EmailField(label='Email', max_length=255)
    assunto = forms.CharField(label='Assunto', max_length=255)
    mensagem = forms.CharField(label='Mesagem', widget=forms.Textarea())




