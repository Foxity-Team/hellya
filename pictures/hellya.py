from hellya import *


ширина, высота = 10, 10
холст = создать_холст(ширина, высота, жёлтый) # Создаём холст шириной 10, высотой 10 и холст жёлтого цвета


повторить(холст, 2, 3, 2, вниз)#
повторить(холст, 2, 6, 2, вниз)# Эти строки рисуют глаза


красить_пиксель(холст, 1, 5, чёрный) #
повторить(холст, 6, 2, 6, вперёд) # Эти строки рисуют рот
красить_пиксель(холст, 8, 5, чёрный) #


сохранить(холст, в50раз) # Сохраняем холст