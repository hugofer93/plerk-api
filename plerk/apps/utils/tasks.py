from django_celery_beat.models import (
    CrontabSchedule,
    IntervalSchedule,
    PeriodicTask,
)


def register_or_update_task(task_name, task_path, schedule):
    """Register or update scheduled task.

    Args:
        task_name (str): Task name.
        task_path (str): Task path.
        schedule (CrontabSchedule, IntervalSchedule):
            if CrontabSchedule: Scheduling by date, hour and minute.
            if IntervalSchedule: Time interval scheduling.

    Returns:
        PeriodicTask: Periodic task instance.
    """
    default_values = {
        'name': task_name,
        'task': task_path,
        'crontab': None,
        'interval': None,
    }

    is_crontab_schedule = isinstance(schedule, CrontabSchedule)
    is_interval_schedule = isinstance(schedule, IntervalSchedule)

    if is_crontab_schedule: default_values['crontab'] = schedule
    if is_interval_schedule: default_values['interval'] = schedule

    periodic_task = PeriodicTask.objects.update_or_create(
        name=task_name,
        task=task_path,
        defaults=default_values,
    )
    return periodic_task
