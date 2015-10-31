#coding: utf-8
from django.core.exceptions import ValidationError


from django.db import models

#Importa o sendmail do django
from django.core.mail import send_mail

# Este dicionário contem os padrões de mensagens de email
classification = {
    'web' :
        {'subject': 'Obrigado por se candidatar',
        'body' : 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Front-End entraremos em contato.'
        },
    'backend' :
        {'subject': 'Obrigado por se candidatar',
        'body' : 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Back-End entraremos em contato.'
        },
    'mobile' :
        {'subject': 'Obrigado por se candidatar',
        'body' : 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador Mobile entraremos em contato.'
        },
    'generic' :
        {'subject': 'Obrigado por se candidatar',
        'body' : 'Obrigado por se candidatar, assim que tivermos uma vaga disponível para programador entraremos em contato.'
        }
}

#Validadores de modelo
def validate_number(value):
    if (value < 0 and value > 10):
        raise ValidationError('%s não é valido' % value)

# Candidate model - Cria o modelo e métodos para o objeto
class Candidate(models.Model):
    # Geramos os valores aceitos
    # Informação necessária do objeto
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    # Conhecimentos do Candidato
    html_grade = models.IntegerField(validators=[validate_number],default=0)
    css_grade = models.IntegerField(validators=[validate_number],default=0)
    javascript_grade = models.IntegerField(validators=[validate_number],default=0)
    python_grade = models.IntegerField(validators=[validate_number],default=0)
    django_grade = models.IntegerField(validators=[validate_number],default=0)
    ios_grade = models.IntegerField(validators=[validate_number],default=0)
    android_grade = models.IntegerField(validators=[validate_number],default=0)

    def clean(self):
        if (self.html_grade or self.css_grade or self.javascript_grade or self.python_grade or self.django_grade or self.ios_grade or self.android_grade) < 0:
            raise ValidationError('Valor tem que ser maior que 0')
        if (self.html_grade or self.css_grade or self.javascript_grade or self.python_grade or self.django_grade or self.ios_grade or self.android_grade) > 10:
            raise ValidationError('Valor tem que ser menor que 11')


    def classificate(self):
        #Antes de avaliar já vamos definir a verdade para generic, caso ele passe por pelo menos uma das avaliações não será enviado
        generic = True
        # Desenvolvedor Web
        if (self.html_grade and self.css_grade and self.javascript_grade) >= 7:
             send_mail(classification['web']['subject'], classification['web']['body'], 'alexandre.sebrao@gmail.com', [self.email], fail_silently=False)
             generic = False
        if (self.python_grade and self.django_grade)  >= 7:
             send_mail(classification['backend']['subject'], classification['backend']['body'], 'alexandre.sebrao@gmail.com', [self.email], fail_silently=False)
             generic = False
        if (self.ios_grade and self.android_grade) >= 7:
            send_mail(classification['mobile']['subject'], classification['mobile']['body'], 'alexandre.sebrao@gmail.com', [self.email], fail_silently=False)
            generic = False
        if generic:
            send_mail(classification['generic']['subject'], classification['generic']['body'], 'alexandre.sebrao@gmail.com', [self.email], fail_silently=False)
