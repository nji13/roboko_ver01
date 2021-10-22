# ロギングコンフィグ 別ファイル（ligging.ini）で読み込んで表示する。別ファイルを読み込まなくてもこちらのファイルに記述して読み込むこともできる
import logging.config


logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')