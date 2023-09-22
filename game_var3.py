from time import time

"""The function takes one argument 'number', which is a guessed number (by default == 1)
and returns the number of tries, which are necessary to guess the number.
If the number is not guessed correctly within 20 tries, the function returns -1."""

def game_core_v3(number: int = 1) -> int:

#определяем минимальное и максимальное число и устанавливаем счетчик попыток

    min_num = 1    
    max_num = 100
    count = 0

# используем алгоритм бинарного поиска. Пока min_num <= max_num:
# вычисляем среднее значение mid_num между min_num и max_num.
  

    while min_num <= max_num:
        count += 1
        mid_num = (min_num + max_num) // 2

        # Если mid_num равно загаданному числу, то угадали и возвращаем число попыток.

        if mid_num == number:
            return count

        #  Если mid_num меньше загаданного числа, то изменяем min_num на mid_num + 1. 
           
        elif mid_num < number:
            min_num = mid_num + 1

        #  Если mid_num больше загаданного числа, то изменяем max_num на mid_num - 1.
        else: 
            max_num = mid_num - 1

    return -1

print('Run benchmarking for game_core_v3: ', game_core_v3(50))
print('Run benchmarking for game_core_v3: ', game_core_v3(1))
print('Run benchmarking for game_core_v2: ', game_core_v3(100))

time.time(game_core_v3)