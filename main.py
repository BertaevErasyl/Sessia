from old_logger import OldLogger
from adapter import NewLoggerAdapter

choice = input("Выберите систему логирования (old/new): ")

if choice.lower() == "old":
    logger = OldLogger()
    print("Используется старая система логирования.")
else:
    logger = NewLoggerAdapter()
    print("Используется новая система логирования.")

logger.log_info("Программа запущена")
logger.log_warning("Недостаточно памяти")
logger.log_error("Ошибка подключения к серверу")