import logging
import random
import time

import json_log_formatter


class CustomFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        extra['message'] = message

        extra['ip'] = {
            'one2four': random.choice(range(5))
        }

        if 'time' not in extra:
            extra['time'] = time.time()

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra
