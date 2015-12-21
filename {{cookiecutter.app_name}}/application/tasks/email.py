from flask.ext.mail import Message

from webapp import app, celery, mail


@celery.task
def send_email(subject, recipients, html=None, text=None):
    with app.app_context(), mail.connect() as conn:
        for recipient in recipients:
            msg = Message(subject,
                          sender=app.config['EMAIL_FROM'],
                          recipients=[recipient, ])
            msg.html = html
            msg.text = text

            conn.send(msg)
