from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=255)
    email = forms.EmailField(label='Email', max_length=255)
    assunto = forms.CharField(label='Assunto', max_length=255)
    mensagem = forms.CharField(label='Mesagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE=mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        mail = EmailMessage(
            subject='Email enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()



