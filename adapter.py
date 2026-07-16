from logger import ILogger
from cloud_logger import CloudLogger

class NewLoggerAdapter(ILogger):

    def __init__(self):
        self.cloud = CloudLogger()

    def log_info(self, message):
        self.cloud.write_info(message)

    def log_warning(self, message):
        self.cloud.write_warn(message)

    def log_error(self, message):
        self.cloud.write_exception(message)