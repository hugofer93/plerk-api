from django.core.cache import cache
from django_celery_beat.models import IntervalSchedule

from plerk import celery_app
from plerk.apps.transactions.models import Transaction
from plerk.apps.utils.tasks import register_or_update_task


schedule_for_sum_price_success_transactions, _ = IntervalSchedule.objects\
    .get_or_create(every=30, period=IntervalSchedule.MINUTES)

@celery_app.task()
def calculate_sum_price_success_transactions():
    total_price = Transaction.objects.get_sum_price_success_transactions()
    cache.set('sum_price_success_transactions', str(total_price), 60*30)

task_name = 'Sum price of successful transactions'
task_path = 'plerk.apps.transactions.tasks'\
            '.calculate_sum_price_success_transactions'
register_or_update_task(
    task_name, task_path,
    schedule_for_sum_price_success_transactions
)


schedule_for_sum_price_rejected_transactions, _ = IntervalSchedule.objects\
    .get_or_create(every=30, period=IntervalSchedule.MINUTES)

@celery_app.task()
def calculate_sum_price_rejected_transactions():
    total_price = Transaction.objects.get_sum_price_rejected_transactions()
    cache.set('sum_price_rejected_transactions', str(total_price), 60*30)

task_name = 'Sum price of rejected transactions'
task_path = ('plerk.apps.transactions.tasks'
            '.calculate_sum_price_rejected_transactions')
register_or_update_task = (
    task_name, task_path,
    schedule_for_sum_price_rejected_transactions
)
