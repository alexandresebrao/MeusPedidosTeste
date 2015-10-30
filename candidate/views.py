#coding: utf-8
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.forms import EmailField
from django.core.exceptions import ValidationError
from candidate.models import Candidate

def isEmailAddressValid( email ):
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False

def new(request):
    template = loader.get_template('new.html')
    context_content = {}
    # Aqui retornamos mensagens em caso de error
    messages = []
    if request.POST:
        # Vamos Ver se o nome é maior que 5!
        #Consideramos que o formulario é valido
        valid = True
        if len(request.POST['fullname'])<= 5:
            valid = False
            messages.append('Seu nome não é valido, o tamanho dele não deve ser menor que 5')
        if not (isEmailAddressValid(request.POST['email'])):
            valid = False
            messages.append('Seu email não é valido')
        if valid:
            candidate = Candidate()
            #Passamos os valores para o objeto
            candidate.fullname = request.POST['fullname']
            candidate.email = request.POST['email']
            candidate.html_grade = int(request.POST['html_grade'])
            candidate.javascript_grade = int(request.POST['javascript_grade'])
            candidate.css_grade = int(request.POST['css_grade'])
            candidate.python_grade = int(request.POST['python_grade'])
            candidate.django_grade = int(request.POST['django_grade'])
            candidate.ios_grade = int(request.POST['ios_grade'])
            candidate.android_grade = int(request.POST['android_grade'])

            try:
                #Salvamos os registros dos candidatos
                candidate.save()
                #Vamos classifica-lo e enviar email!
                candidate.classificate()
            except:
                print "ERROR"
            context_content['candidate'] = candidate
            template = loader.get_template('finish.html')
        else:
            context_content['errors'] = messages
    context = RequestContext(request, context_content)
    return HttpResponse(template.render(context))
