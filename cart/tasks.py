from celery.app import task
from django.core.mail import send_mail
from .models import OrderProduct


@task
def order_payed(order_id):
    """
    Отправка уведомления после оплаты заказа
    """
    order = OrderProduct.objects.get(id=order_id)
