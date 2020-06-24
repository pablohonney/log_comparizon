import logging
import setup  # initialize logger.

logger = logging.getLogger(__name__)

wrong_msg = {
    'foobar': 'foo',
    'foo': 'Hello',
    'bar': 'world',
    'baz': 42,
}

correct_msg = {
    'foobar': {
        'foo': 'I am string',
        'bar': [{
            "whole": 12,
        }]
    }
}

logger.info(wrong_msg)
logger.info(correct_msg)

# TODO TBD
# try:
#     raise ValueError('something wrong')
# except ValueError as e:
#     # logger.error('Request failed', exc_info=True)
#     logger.error('Request failed', exc_info=True)
