# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 15. Цикл while: количество цифр числа
 Вход: 
   12345
 Результат:
   Цифр в числе: 5
"""
n = int( input("Введите целое число: ") )
count = 0
while n > 0:
  n = n // 10
  count += 1
print ( "Цифр в числе:", count )