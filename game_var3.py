from time import time

"""The function takes one argument 'number', which is a guessed number (by default == 1)
and returns the number of tries, which are necessary to guess the number.
If the number is not guessed correctly within 20 tries, the function returns -1."""

def game_core_v3(number: int = 1) -> int:

#���������� ����������� � ������������ ����� � ������������� ������� �������

    min_num = 1    
    max_num = 100
    count = 0

# ���������� �������� ��������� ������. ���� min_num <= max_num:
# ��������� ������� �������� mid_num ����� min_num � max_num.
  

    while min_num <= max_num:
        count += 1
        mid_num = (min_num + max_num) // 2

        # ���� mid_num ����� ����������� �����, �� ������� � ���������� ����� �������.

        if mid_num == number:
            return count

        #  ���� mid_num ������ ����������� �����, �� �������� min_num �� mid_num + 1. 
           
        elif mid_num < number:
            min_num = mid_num + 1

        #  ���� mid_num ������ ����������� �����, �� �������� max_num �� mid_num - 1.
        else: 
            max_num = mid_num - 1

    return -1

print('Run benchmarking for game_core_v3: ', game_core_v3(50))
print('Run benchmarking for game_core_v3: ', game_core_v3(1))
print('Run benchmarking for game_core_v2: ', game_core_v3(100))

time.time(game_core_v3)