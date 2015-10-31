#coding: utf-8
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.forms import EmailField
from django.core.exceptions import ValidationError
from candidate.models import Candidate

#Validamos o Email aqui :D
def isEmailAddressValid( email ):
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False

#Esta view cria o cadastro e carrega o formulario, e controla o POST e verifica o conteudo postado
def new(request):
    template = loader.get_template('new.html')
    context_content = {}
    # Aqui retornamos mensagens em caso de error
    messages = []
    candidate = Candidate()
    #se o formulario foi postado
    if request.POST:
        # Vamos Ver se o nome é maior que 5!
        #Consideramos que o formulario é valido
        valid = True

        #Populamos o modelo com os objetos


        candidate.fullname = request.POST['fullname']
        candidate.email = request.POST['email']
        candidate.html_grade = int(request.POST['html_grade'])
        candidate.javascript_grade = int(request.POST['javascript_grade'])
        candidate.css_grade = int(request.POST['css_grade'])
        candidate.python_grade = int(request.POST['python_grade'])
        candidate.django_grade = int(request.POST['django_grade'])
        candidate.ios_grade = int(request.POST['ios_grade'])
        candidate.android_grade = int(request.POST['android_grade'])

        if len(candidate.fullname)<= 5:
            valid = False
            messages.append('Seu nome não é valido, o tamanho dele não deve ser menor que 5')
        if not (isEmailAddressValid(candidate.email)):
            valid = False
            messages.append('Seu email não é valido')
        if valid:

            #Passamos os valores para o objeto

            candidate.save()
            #Vamos classifica-lo e enviar email!
            candidate.classificate()
            context_content['candidate'] = candidate
            template = loader.get_template('finish.html')
        else:
            context_content['errors'] = messages
    context_content['candidate'] = candidate
    context = RequestContext(request, context_content)
    return HttpResponse(template.render(context))
