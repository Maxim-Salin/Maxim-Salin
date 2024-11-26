def send_email(message, recipient, sender="university.help@gmail.com"):
    if ((str(recipient).find('.com') != -1) or \
        (str(recipient).find('.net') != -1)) and \
            (str(recipient).find('@') != -1):
        if str(recipient) == sender:
            print('Нельзя отправить письмо самому себе!')
            # return False
        else:
            if sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено  {recipient}")
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


    # return False
    else:
        print('error recipiend')

send_email('hello', 'max@gmail.net', "max.salin@yandex.ru")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')