from new_shop.celery import app
from django.core.mail import send_mail
from authorization.models import User
from rest_framework.authtoken.models import Token
from new_shop.settings import EMAIL_HOST_USER

@app.task(serializer='json')
def mail_for_new_user(get_user=None, **kwargs):
    token = Token.objects.create(user=get_user)
    subject = "Wellcome, {}".format(token.user.first_name)
    massage = "Now, you are with as! Your password is {}.".format(token.user.password)
    mail_sent = send_mail(subject, massage, EMAIL_HOST_USER, [token.user.email], fail_silently=True,)
    return mail_sent