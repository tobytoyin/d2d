import logging
import pprint


class PrettyPrintFormatter(logging.Formatter):
    def format(self, record):
        # Use pprint to format the log message
        formatted_message = pprint.pformat(record.getMessage())
        record.msg = formatted_message
        return super().format(record)


def setup_custom_logger(name):
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


def setup_service_logger(service_name: str):
    logger = logging.getLogger(service_name)
    logger.setLevel(logging.INFO)

    fmt = "[%(levelname)s]@%(module)s\n%(message)s\n"
    handler = logging.StreamHandler()
    handler.setFormatter(PrettyPrintFormatter(fmt=fmt))
    logger.addHandler(handler)

    logger.propagate = False

    return logger
