import os
import json
import logging.config
from typing import Any
from tkww_api.utils.utils import load_logging_config


class Logger:

    def __init__(self):
        """
        Initializes the Logger class.

        This method sets up the logger instance and retrieves the worker ID.
        """
        self.logger = logging.getLogger("app")
        self.worker_id = os.getpid()

    def init_app(self, app: Any):
        """Initialize the logger for the given app instance.

        This method loads the logging configuration from the config.yml file and configures the logger.

        Args:
            app (Any): app instance.
        """
        config = load_logging_config("tkww_api/utils/logging_config/config.yml")
        logging.config.dictConfig(config)

    def _build_log_message(self, msg: str, ip: str = "N/A"):
        """Builds a log message with the given message and IP address.

        Args:
            msg (str): The message to be included in the log.
            ip (str, optional): The IP address associated with the log message. Defaults to "N/A".

        Returns:
            str: The log message in JSON format.
        """
        logMessage = {"ip": ip, "worker_id": self.worker_id, "custom_msg": msg}
        return json.dumps(logMessage)

    def info(self, msg: str):
        """Log an informational message.

        Args:
            msg (str): The message to be logged.
        """
        self.logger.info(msg)

    def error(self, msg: str):
        """Logs an error message.

        Args:
            msg (str): The error message to be logged.
        """
        self.logger.error(msg)

    def info_custom(self, msg: str, ip: str = "N/A"):
        """Logs an info message with custom information.

        Args:
            msg (str): The message to be logged.
            ip (str, optional): The IP address associated with the log message. Defaults to "N/A".
        """
        self.logger.info(self._build_log_message(msg, ip))

    def error_custom(self, msg: str, ip: str = "N/A"):
        """Logs a custom error message with an optional IP address.

        Args:
            msg (str): The error message to be logged.
            ip (str, optional): The IP address associated with the error. Defaults to "N/A".
        """
        self.logger.error(self._build_log_message(msg, ip))


Log = Logger()
