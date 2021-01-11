"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging
import logtest
formatter = '%(levelname)s:%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

logger = logging.getLogger(__name__)
logging.info('info {}'.format('main'))

logtest.do_something()
