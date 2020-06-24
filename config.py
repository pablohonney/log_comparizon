import logging.config
import json

log_schema = {
    "type": "object",
    "properties": {
        "foobar": {
            "type": "object",
            "properties": {
                "foo": {
                    "type": "string"
                },
                "bar": {
                    "type": "array",
                    "maxItems": 1,
                    "items": {
                        "type": "object",
                        "properties": {
                            "number": {
                                "type": "number"
                            },
                        },
                    },
                },
            },
        }
    },
}

format_string = json.dumps({
    'name': '%(name)s',
    'lineno': '%(lineno)s',
    'data': '%(msg)s',
})

config = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'plain_formatter': {
            'format': format_string,
            'class': 'formatters.plain_formatter.CustomFormatter',
        },
        'python_json_logger': {
            'format': format_string,
            'class': 'formatters.python_json_logger.CustomFormatter',
        },
        # 'json_log_formatter': {
        #     'format': format_string,
        #     'class': 'formatters.json_log_formatter.CustomFormatter',
        # },
    },
    'filters': {
        'schema_filter': {
            '()': 'schema_filter.JsonSchemaFilter',
            'schema': log_schema,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'plain_formatter',
            'class': 'logging.StreamHandler',
            'filters': [
                'schema_filter'
            ],
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'plugins': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        }
    },
}
logging.config.dictConfig(config)
