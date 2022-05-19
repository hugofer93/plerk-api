from django.core.cache import cache
from django.utils.timezone import now as datetime_now
from django_celery_beat.models import IntervalSchedule, PeriodicTask

from plerk import celery_app
from plerk.apps.companies.models import Company
from plerk.apps.utils.tasks import register_or_update_task


schedule_for_company_with_more_sales, _ = IntervalSchedule.objects\
    .get_or_create(every=30, period=IntervalSchedule.MINUTES)

@celery_app.task()
def calculate_company_with_more_sales():
    company = Company.objects.get_company_with_more_sales()
    cache.set('company_id_with_more_sales', company.id, 60*30)

task_name = 'Calculate company with more sales'
task_path = 'plerk.apps.companies.tasks.calculate_company_with_more_sales'
register_or_update_task(
    task_name, task_path,
    schedule_for_company_with_more_sales
)


schedule_for_company_with_less_sales, _ = IntervalSchedule.objects\
    .get_or_create(every=30, period=IntervalSchedule.MINUTES)

@celery_app.task()
def calculate_company_with_less_sales():
    company = Company.objects.get_company_with_less_sales()
    cache.set('company_id_with_less_sales', company.id, 60*30)

task_name = 'Calculate company with less sales'
task_path = 'plerk.apps.companies.tasks.calculate_company_with_less_sales'
register_or_update_task(
    task_name, task_path,
    schedule_for_company_with_less_sales
)


schedule_for_company_with_most_rejected_sales, _ = IntervalSchedule.objects\
    .get_or_create(every=30, period=IntervalSchedule.MINUTES)

@celery_app.task()
def calculate_company_with_most_rejected_sales():
    company = Company.objects.get_company_with_most_rejected_sales()
    cache.set('company_id_with_most_rejected_sales', company.id, 60*30)

task_name = 'Calculate company with most rejected sales'
task_path = 'plerk.apps.companies.tasks'\
            '.calculate_company_with_most_rejected_sales'
register_or_update_task(
    task_name, task_path,
    schedule_for_company_with_most_rejected_sales
)


schedule_for_company_with_less_rejected_sales, _ = IntervalSchedule.objects\
    .get_or_create(every=30, period=IntervalSchedule.MINUTES)

@celery_app.task()
def calculate_company_with_less_rejected_sales():
    company = Company.objects.get_company_with_less_rejected_sales()
    cache.set('company_id_with_less_rejected_sales', company.id, 60*30)

task_name = 'Calculate company with less rejected sales'
task_path = 'plerk.apps.companies.tasks'\
            '.calculate_company_with_less_rejected_sales'
register_or_update_task(
    task_name, task_path,
    schedule_for_company_with_less_rejected_sales
)
