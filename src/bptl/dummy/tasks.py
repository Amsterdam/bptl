import logging

from bptl.tasks.models import BaseTask
from bptl.tasks.registry import register

logger = logging.getLogger(__name__)


@register
def dummy(task: BaseTask) -> {}:
    """
    A dummy task to demonstrate the registry machinery.

    The task receives the :class:`ExternalTask` instance and logs some information,
    after which it completes the task.
    """
    task_id = getattr(task, "task_id", task.id)

    logger.info("Received external task: %s", task_id)
    logger.info("External task currently has the variables: %r", task.get_variables())
    return {}
