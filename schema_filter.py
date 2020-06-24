import logging

from jsonschema import validate, ValidationError


class JsonSchemaFilter(logging.Filter):
    def __init__(self, schema, name=''):
        super(JsonSchemaFilter, self).__init__(name)
        self._schema = schema

    def filter(self, record):
        try:
            validate(record.msg, self._schema)
        except ValidationError as e:
            # print(e)
            return False

        return super(JsonSchemaFilter, self).filter(record)
