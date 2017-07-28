# -*- coding: utf-8 -*-

# Количество машин
cars = 100
# Количество мест в машине
space_in_a_car = 4.0
# Количество водителей
drivers = 30
# Количество пассажиров
passengers = 90
# Количество машины без водителей
cars_not_driven = cars - drivers
# Машины с водителями
cars_driven = drivers
# Количество пассажиров
carpool_capacity = cars_driven * space_in_a_car
# Количество пассажиров в машине
average_passengers_per_car = passengers / cars_driven

print u"В наличии", cars, u"автомобилей."
print u"И только", drivers, u"водителей вышли на работу."
print u"Получается, что", cars_not_driven, u"машин пустуют."
print u"Мы можем перевести сегодня", carpool_capacity, u"человек."
print u"Сегодня нужно отвезти", passengers, u"человек."
print u"В каждой машине будет примерно", average_passengers_per_car, u"человека."
