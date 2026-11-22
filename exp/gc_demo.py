
import gc
import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Очищаем старый мусор перед экспериментом
gc.collect()

# Запоминаем состояние сборщика
was_enabled = gc.isenabled()

# Отключаем автоматическую сборку циклов
gc.disable()

try:
    # Создаём два узла
    a = Node('A')
    b = Node('B')

    # Связываем их в кольцо
    a.next = b
    b.next = a

    # Создаём слабые ссылки
    weak_a = weakref.ref(a)
    weak_b = weakref.ref(b)

    # Удаляем обычные ссылки
    del a
    del b

    print('До ручной сборки:')
    print('Объект A жив:', weak_a() is not None)
    print('Объект B жив:', weak_b() is not None)

    # Принудительно запускаем сборщик
    collected = gc.collect()

    print('\nПосле ручной сборки:')
    print('Объект A жив:', weak_a() is not None)
    print('Объект B жив:', weak_b() is not None)
    print('Собрано объектов:', collected)

finally:
    # Возвращаем исходное состояние сборщика
    if was_enabled:
        gc.enable()