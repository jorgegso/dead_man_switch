#!usr/bin/env python3

import time
import smtplib

# Configuración del correo electrónico
sender_email = "tu_email@gmail.com"
receiver_emails = ["destinatario1_email@gmail.com", "destinatario2_email@gmail.com"]
password = input("Ingrese la contraseña de su correo electrónico y presione Enter: ")

# Tiempo de espera en segundos
waiting_time = 60

# Bucle infinito
while True:
    # Espera por el tiempo especificado
    time.sleep(waiting_time)


    print("☠️ - Se ha realizado una acción - ☠️")

    # Realiza alguna acción aquí...


    print("☠️ - Se ha enviado un correo electrónico - ☠️")

    # Envía el correo electrónico
    message = "Este es un mensaje de prueba del Dead Man's Switch."
    for receiver_email in receiver_emails:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print(f"☠️ - Correo electrónico enviado a {receiver_email} - ☠️")

