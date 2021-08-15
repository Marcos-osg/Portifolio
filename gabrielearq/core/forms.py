from django.forms import ModelForm
from core.models import Contato


class FormContato(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_contato')
        email = data.get('email_contato')
        assunto = data.get('assunto_contato')
        mensagem = data.get('mensagem_contato')



    class Meta:
        model = Contato
        fields = ('__all__')
