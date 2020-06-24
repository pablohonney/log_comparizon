import logging.config
import json


class CustomFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        if record.msg:
            record.msg = json.dumps(record.msg)
        return super(CustomFormatter, self).format(record)
