from old_logger import OldLogger
from adapter import NewLoggerAdapter

old_logger = OldLogger()
new_logger = NewLoggerAdapter()

print("===== СТАРАЯ СИСТЕМА ЛОГИРОВАНИЯ =====")
old_logger.log_info("Программа запущена")
old_logger.log_warning("Недостаточно памяти")
old_logger.log_error("Ошибка подключения к серверу")

print("\n===== НОВАЯ СИСТЕМА ЛОГИРОВАНИЯ =====")
new_logger.log_info("Программа запущена")
new_logger.log_warning("Недостаточно памяти")
new_logger.log_error("Ошибка подключения к серверу")