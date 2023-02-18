import logging


def create_logger(app, name):
    """
    Create and configurate logger
    :param app: instance application Flask
    :param name: logger name
    :return: None
    """
    # get logger
    logger = logging.getLogger(name)
    # set level
    logger.setLevel(logging.INFO)
    # configurate file handler
    file_handler = logging.FileHandler(app.config.get(f"{name.upper()}_LOG_PATH"), encoding="UTF-8")
    # configurate formatter for file handler
    file_format = logging.Formatter(app.config.get('LOG_FORMAT'), datefmt=app.config.get("DATE_FORMAT"))
    # set formatter to file handler
    file_handler.setFormatter(file_format)
    # add file handler to logger
    logger.addHandler(file_handler)
