# フィルタ設定 任意の文字列が含まれていた場合、表示させない

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

class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.info('from main')
logger.info('from main password = "test"')