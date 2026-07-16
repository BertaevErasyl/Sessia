from logger import ILogger

class OldLogger(ILogger):

    def log_info(self, message):
        print("[СТАРАЯ СИСТЕМА][ИНФОРМАЦИЯ]:", message)
        with open("old_logs.txt", "a", encoding="utf-8") as file:
            file.write("[ИНФОРМАЦИЯ] " + message + "\n")

    def log_warning(self, message):
        print("[СТАРАЯ СИСТЕМА][ПРЕДУПРЕЖДЕНИЕ]:", message)
        with open("old_logs.txt", "a", encoding="utf-8") as file:
            file.write("[ПРЕДУПРЕЖДЕНИЕ] " + message + "\n")

    def log_error(self, message):
        print("[СТАРАЯ СИСТЕМА][ОШИБКА]:", message)
        with open("old_logs.txt", "a", encoding="utf-8") as file:
            file.write("[ОШИБКА] " + message + "\n")