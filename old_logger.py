from logger import ILogger

class OldLogger(ILogger):

    def log_info(self, message):
        print("[СТАРАЯ СИСТЕМА][ИНФОРМАЦИЯ]:", message)

    def log_warning(self, message):
        print("[СТАРАЯ СИСТЕМА][ПРЕДУПРЕЖДЕНИЕ]:", message)

    def log_error(self, message):
        print("[СТАРАЯ СИСТЕМА][ОШИБКА]:", message)