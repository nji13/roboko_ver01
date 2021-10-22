# logを送る

import logging
import logging.handlers

smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'jetfield@hotmail.co.jp'
to_email = 'jetfield@hotmail.co.jp'
username = 'jetfield@hotmail.co.jp'
password = 'crea1021'

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log', credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))

logger.info('test')
logger.critical('critical')