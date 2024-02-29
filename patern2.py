import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Перевірка, чи вже існує екземпляр класу
        with cls._lock:
            if cls not in cls._instances:
                # Створення нового екземпляру класу, якщо він ще не існує
                instance = super().__call__(*args, **kwargs)
                # Зберігання створеного екземпляру
                cls._instances[cls] = instance
        return cls._instances[cls]

# Приклад класу Singleton
class Singleton(metaclass=SingletonMeta):
    def __init__(self, name):
        self.name = name

# Приклад використання:
s1 = Singleton("Instance 1")
s2 = Singleton("Instance 2")

print(s1.name)  # Виведе: Instance 1
print(s2.name)  # Виведе: Instance 1 (використовує той самий екземпляр)

print(s1 is s2)  # Виведе: True (обидва змінні посилаються на один і той же об'єкт)
