class CloudLogger:

    def write_info(self, message):
        print("[ОБЛАЧНОЕ ХРАНИЛИЩЕ][ИНФОРМАЦИЯ]:", message)

    def write_warn(self, message):
        print("[ОБЛАЧНОЕ ХРАНИЛИЩЕ][ПРЕДУПРЕЖДЕНИЕ]:", message)

    def write_exception(self, message):
        print("[ОБЛАЧНОЕ ХРАНИЛИЩЕ][ОШИБКА]:", message)