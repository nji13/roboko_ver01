# loggerでsetlevelを設定する（別ファイルlesson_logging_logtest.py）

"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging

import lesson_logging_logtest as lo

logging.basicConfig(level=logging.INFO) #ここでlevelをINFOに設定してもlogger.setLevelで各々レベルを設定できる

logging.info('info')

lo.do_something()