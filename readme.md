# django1 - projeto web simples

Desenvolvimento de um CRUD de produtos utilizando Python e Django, como descrito 
no curso https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/.
O Objetivo deste projeto, foi estudar e praticar a criação de formulários no django, utilizando forms.py, configurações de envio de email, 
conexão com o MySQL e autenticação simples de usuário. 

## Para rodar a app: 

```bash
python -m venv venv
```

```bash
Linux:
source venv/bin/activate
OU
. venv/bin/activate
```

```bash
Windows:
.\venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py runserver
```

## Criando um usuário no painel admin:

```bash
python manage.py createsuperuser
```

- Após a criação do superuser, basta rodar a app e digitar no final do 
localhost:8000/admin para realizar o login. 
- Para cadastrar um produto, basta digitar localhost:8000/produto. 
- É necessário estar logado via admin, caso não esteja, será redirecionado para a home.
- A url localhost:8000/contato exibe um formulário para envio de email. As configurações de envio de 
email estão comentadas, pois não foi configurado um servidor de envio de email válido. 
- O banco de dados configurado é o SQLite3, porém o MySQL também está configura, para usá-lo, basta 
descomentar as configurações em settings.py 

#### Dependências:
- python: 3.11.6
- django: 4.2.8