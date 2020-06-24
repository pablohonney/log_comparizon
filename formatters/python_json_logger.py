from pythonjsonlogger import jsonlogger


# FIXME doesn't support fmt string in the ctor
class CustomFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomFormatter, self).add_fields(log_record, record, message_dict)
