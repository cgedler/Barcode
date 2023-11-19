from django.test import TestCase

# Create your tests here.

from datetime import date
from django.db.models import Q

from barcode.models.mbultos import Bulto
from barcode.models.mguia import Guia

today = date.today()
query_a = 'CCS'
query_b = 'PLACA1'

try:
    results = Bulto.objects.filter(Q(origen__icontains=query_a) & Q(camion__icontains=query_b) & Q(estado='1') & Q(modified__contains=today))
    total_bultos_cargados = results.count()
    #print(results)
    print('total bultos cargados: ' + str(total_bultos_cargados))
    result_dict = {}
    keys_dict = []
    for result in results:
        #print(result.guias)
        if not result.guias in keys_dict:
            keys_dict.append(result.guias) 
    result_dict = dict.fromkeys(keys_dict)
    total_guias_cargados = str(len(keys_dict))

    #datos_guia = []
    #total_bultos_guia = ''

    for key in result_dict:
            #result_dict[key].add('bulto')
            
            datos_guia = []
            result_guia = Guia.objects.filter(Q(id_guia__exact=key))
            # print(result_guia)
            for result_b in result_guia:
                datos_guia.append(result_b.cantidad) # Datos de la guia total de bultos
                #datos_guia.append(result_b.destino)

            #i = 0
                result_bultos = results.filter(guias=key)
                total_bultos_guia = result_bultos.count()
                #print(total_bultos_guia)
            #for item_bulto in results.filter(guias=key):
                #dict.update(newkey1 ='portal')  
                #result_dict[key]['bulto'].append(item_bulto.id_bulto)
            #    i = i + 1
                
            #total_bultos_guia = i
                datos_guia.append(total_bultos_guia)

                result_dict[key] = datos_guia #item_bulto.id_bulto #Aqui agrego al diccionario principal

    print('total guias cargados: ' + str(total_guias_cargados))
    ####print('total bultos guias cargados: ' + str(total_bultos_guia))
    #print(result_dict)
    for key, value in result_dict.items():
        print (key, value)
        for x in value:
            print(x[0])
            print(x[1])
except Exception as e:
    print(e)

#for i in USucursal.objects.filter(usuario=1):
#    print(i.sucursal)
    
#    try:
#        for a in Remitente.objects.filter(origen=i.sucursal):  #'CCS'):#i.sucursal):
#            print(a)
#    except Exception as e:
#            print(e)

#b.entries.count()
#print([e.pub_date for e in Entry.objects.all()])

#query = "BNAD7900000000040004"
#print(query)

#query_a = Bulto.objects.filter(id_bulto__icontains=query)
#var_guia = query_a[0].guias
#print(var_guia)

#try:
#    query_a = Bulto.objects.filter(id_bulto__icontains=query)
#    valor_0 = query_a[0].estado
#    var_guia = query_a[0].guias
    #print(valor_0)
#    query_b = Bulto.objects.filter(Q(guias__icontains=var_guia) & Q(estado="0")) 
#    send_email = query_b.count()
#    print(str(send_email))
#    if send_email == 0:
#        print("Puede enviar correos")
#        print("Guia n#: " + str(var_guia))
#        query_c = Guia.objects.filter(id_guia__icontains=var_guia)
        #query_c = Guia.objects.raw('SELECT * FROM guia WHERE id_guia = %s', [var_guia])
        #val_remitente = query_c[0].remitente
        #val_remitente = query_c[0].remitente
#        val_remitente = query_c[0].remitente
#        str_val_remitente = str(val_remitente)
#        remitente_id = int(str_val_remitente[0:9])
        #val_remitente_b = val_remitente
#        print(val_remitente)
#        print(remitente_id)
        #print("Remitente: " + str(val_remitente))
        #print("Remitente: " + str(val_remitente) + str(val_remitente_b))
#        query_d = Remitente.objects.filter(id_remitente__icontains=remitente_id)
#        correo_r = query_d[0].email
#        print(correo_r)

#    i = 0
#    for r in query_b:
#        print(query_b[i].id_bulto)
#        i = i + 1

#    if valor_0 == '0':
#        Bulto.objects.filter(id_bulto__icontains=query).update(estado="1")
#    else:
#        print("Campo actualizado")
#except Exception as e:
#    print(e)


# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import *


# message = Mail(
#     from_email='cgedler@gmail.com',
#     to_emails='jogreo.nails@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     #sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)

# class EmailTest(TestCase):
#     def test_send_email(self):
# #         try:
#         subject = 'Thank you for registering to our site'
#         message = ' it  means a world to us '
#         email_from = settings.DEFAULT_FROM_EMAIL

#         recipient_list = ['cgedler@gmail.com']
#         send_mail(subject, message, email_from, recipient_list, fail_silently=False)

#         except Exception as e:
#             print(e)

#subject = 'Thank you for registering to our site'
#message = ' it  means a world to us '
#email_from = settings.EMAIL_HOST_USER

#class EmailTest(TestCase):
#    def test_send_email(self):
    # Send message.
#        recipient_list = ['cgedler@gmail.com']
#        send_mail(subject, message, email_from, recipient_list, fail_silently=False)