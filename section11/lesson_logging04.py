"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging

import lesson_logging_logtest as lo


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logging.info('from main')

lo.do_something()