

from random import randint


import smtplib
from email.message import EmailMessage
import ssl



def sent_email(email_receiver,content):
    email_sender = "secretfriend202212@gmail.com"
    secret_code = "ekshkcoyaswjaley"

    msg = EmailMessage()


    msg['Subject'] = "Asignacion de amigo secreto"
    msg['From'] = email_sender
    msg['to'] = email_receiver
    msg.set_content(f"Tu amigo secreto es {content}")
    msg.add_alternative(f"""\n\n
    
    

    <body style=" border-radius:0.4rem; text-align:center; background-color:black; padding:1rem;">

        <h1 text-align:center; style="color:white;">Tu amigo secreto es</h1>
        <span text-align:center; style="font-size:3.2rem; font-family: 'Ubuntu'; color: white ;  " > {content} </span>
    </body>

    """,subtype="html")


    context  = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,secret_code)
        smtp.sendmail(
            email_sender,
            email_receiver,
            msg.as_string()
        )

def getId(e):
    return e['id']


def secret_friend(friends):

    if not len(friends) > 1:
        print("Minimo 2 amigos.")
        return
    picked_numbers  = {}


    #asigna un numero aleatorio al id de cada amigo.
    for friend in friends:
        random_num = randint(0,len(friends)-1)
        while (random_num in picked_numbers):
            random_num = randint(0,len(friends)-1)

        picked_numbers[random_num] = friend['nombre']
        friend['id'] = random_num


    #ordena la lista de menor a mayor.
    friends.sort(key=getId)

    secret_friends = []
    
    #guarda el primer amigo que se encuentre en la lista.
    
    first_friend = friends[0]


    #ingresa a la lista  una tupla con los dos primeros amigos que se encuentren en a lista.
    #en caso de que solo quede un amigo, se ingresa a la tupla ese ultimo  y el primero leido.
    while len(friends) != 0:
        if len(friends) > 1:
            secret_friends.append(
                (friends.pop(0),friends[0])
            )
        else:
            secret_friends.append((friends.pop(0),first_friend))

    #retorna la lista de amigos.

    return secret_friends


friends = [
    {"nombre":"Jysus","id":0,"email":"jesusfiguera20@gmail.com"},
    {"nombre":"Joel","id":0,"email":"jesusfiguera2310@gmail.com"},
    {"nombre":"Jade","id":0,"email":"figueraj196@gmail.com"},
]


secret_friends  = secret_friend(friends)


for secret in secret_friends:
    #print(f"{secret[0]['nombre']} le regala a {secret[1]['nombre']}")
    sent_email(secret[0]['email'],secret[1]['nombre'])



