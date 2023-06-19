"""
3. Написать функцию host_range_ping_tab(),
возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам,
представленным в табличном формате (использовать модуль tabulate).
Таблица должна состоять из двух колонок и выглядеть примерно так:

Reachable
10.0.0.1
10.0.0.2

Unreachable
10.0.0.3
10.0.0.4

script listing at lines:  35...291
"""


from tabulate import tabulate
from task2 import host_range_ping


def host_range_ping_tab():
    ip_ok, ip_not_ok = host_range_ping(echo=False)
    print('\n Доступны адреса : \n', tabulate(ip_ok))
    print('\n Недоступны адреса :\n', tabulate(ip_not_ok))


if __name__ =='__main__':
    host_range_ping_tab()



"""
Script Listing

(venv) user1@ubuntu:~/Desktop/chat/Lesson_9$ python task3.py
Please enter start IP address : 192.168.1.1
Please enter number of addresses to check : 240
Completed 100%

 Доступны адреса : 
 -  -  -  -  -  -  -  -  -  -  -  -  -
1  9  2  .  1  6  8  .  1  .  1
1  9  2  .  1  6  8  .  1  .  3  4
1  9  2  .  1  6  8  .  1  .  1  3  6
1  9  2  .  1  6  8  .  1  .  1  9  9
-  -  -  -  -  -  -  -  -  -  -  -  -

 Недоступны адреса :
 -  -  -  -  -  -  -  -  -  -  -  -  -
1  9  2  .  1  6  8  .  1  .  2
1  9  2  .  1  6  8  .  1  .  3
1  9  2  .  1  6  8  .  1  .  4
1  9  2  .  1  6  8  .  1  .  5
1  9  2  .  1  6  8  .  1  .  6
1  9  2  .  1  6  8  .  1  .  7
1  9  2  .  1  6  8  .  1  .  8
1  9  2  .  1  6  8  .  1  .  9
1  9  2  .  1  6  8  .  1  .  1  0
1  9  2  .  1  6  8  .  1  .  1  1
1  9  2  .  1  6  8  .  1  .  1  2
1  9  2  .  1  6  8  .  1  .  1  3
1  9  2  .  1  6  8  .  1  .  1  4
1  9  2  .  1  6  8  .  1  .  1  5
1  9  2  .  1  6  8  .  1  .  1  6
1  9  2  .  1  6  8  .  1  .  1  7
1  9  2  .  1  6  8  .  1  .  1  8
1  9  2  .  1  6  8  .  1  .  1  9
1  9  2  .  1  6  8  .  1  .  2  0
1  9  2  .  1  6  8  .  1  .  2  1
1  9  2  .  1  6  8  .  1  .  2  2
1  9  2  .  1  6  8  .  1  .  2  3
1  9  2  .  1  6  8  .  1  .  2  4
1  9  2  .  1  6  8  .  1  .  2  5
1  9  2  .  1  6  8  .  1  .  2  6
1  9  2  .  1  6  8  .  1  .  2  7
1  9  2  .  1  6  8  .  1  .  2  8
1  9  2  .  1  6  8  .  1  .  2  9
1  9  2  .  1  6  8  .  1  .  3  0
1  9  2  .  1  6  8  .  1  .  3  1
1  9  2  .  1  6  8  .  1  .  3  2
1  9  2  .  1  6  8  .  1  .  3  3
1  9  2  .  1  6  8  .  1  .  3  5
1  9  2  .  1  6  8  .  1  .  3  6
1  9  2  .  1  6  8  .  1  .  3  7
1  9  2  .  1  6  8  .  1  .  3  8
1  9  2  .  1  6  8  .  1  .  3  9
1  9  2  .  1  6  8  .  1  .  4  0
1  9  2  .  1  6  8  .  1  .  4  1
1  9  2  .  1  6  8  .  1  .  4  2
1  9  2  .  1  6  8  .  1  .  4  3
1  9  2  .  1  6  8  .  1  .  4  4
1  9  2  .  1  6  8  .  1  .  4  5
1  9  2  .  1  6  8  .  1  .  4  6
1  9  2  .  1  6  8  .  1  .  4  7
1  9  2  .  1  6  8  .  1  .  4  8
1  9  2  .  1  6  8  .  1  .  4  9
1  9  2  .  1  6  8  .  1  .  5  0
1  9  2  .  1  6  8  .  1  .  5  1
1  9  2  .  1  6  8  .  1  .  5  2
1  9  2  .  1  6  8  .  1  .  5  3
1  9  2  .  1  6  8  .  1  .  5  4
1  9  2  .  1  6  8  .  1  .  5  5
1  9  2  .  1  6  8  .  1  .  5  6
1  9  2  .  1  6  8  .  1  .  5  7
1  9  2  .  1  6  8  .  1  .  5  8
1  9  2  .  1  6  8  .  1  .  5  9
1  9  2  .  1  6  8  .  1  .  6  0
1  9  2  .  1  6  8  .  1  .  6  1
1  9  2  .  1  6  8  .  1  .  6  2
1  9  2  .  1  6  8  .  1  .  6  3
1  9  2  .  1  6  8  .  1  .  6  4
1  9  2  .  1  6  8  .  1  .  6  5
1  9  2  .  1  6  8  .  1  .  6  6
1  9  2  .  1  6  8  .  1  .  6  7
1  9  2  .  1  6  8  .  1  .  6  8
1  9  2  .  1  6  8  .  1  .  6  9
1  9  2  .  1  6  8  .  1  .  7  0
1  9  2  .  1  6  8  .  1  .  7  1
1  9  2  .  1  6  8  .  1  .  7  2
1  9  2  .  1  6  8  .  1  .  7  3
1  9  2  .  1  6  8  .  1  .  7  4
1  9  2  .  1  6  8  .  1  .  7  5
1  9  2  .  1  6  8  .  1  .  7  6
1  9  2  .  1  6  8  .  1  .  7  7
1  9  2  .  1  6  8  .  1  .  7  8
1  9  2  .  1  6  8  .  1  .  7  9
1  9  2  .  1  6  8  .  1  .  8  0
1  9  2  .  1  6  8  .  1  .  8  1
1  9  2  .  1  6  8  .  1  .  8  2
1  9  2  .  1  6  8  .  1  .  8  3
1  9  2  .  1  6  8  .  1  .  8  4
1  9  2  .  1  6  8  .  1  .  8  5
1  9  2  .  1  6  8  .  1  .  8  6
1  9  2  .  1  6  8  .  1  .  8  7
1  9  2  .  1  6  8  .  1  .  8  8
1  9  2  .  1  6  8  .  1  .  8  9
1  9  2  .  1  6  8  .  1  .  9  0
1  9  2  .  1  6  8  .  1  .  9  1
1  9  2  .  1  6  8  .  1  .  9  2
1  9  2  .  1  6  8  .  1  .  9  3
1  9  2  .  1  6  8  .  1  .  9  4
1  9  2  .  1  6  8  .  1  .  9  5
1  9  2  .  1  6  8  .  1  .  9  6
1  9  2  .  1  6  8  .  1  .  9  7
1  9  2  .  1  6  8  .  1  .  9  8
1  9  2  .  1  6  8  .  1  .  9  9
1  9  2  .  1  6  8  .  1  .  1  0  0
1  9  2  .  1  6  8  .  1  .  1  0  1
1  9  2  .  1  6  8  .  1  .  1  0  2
1  9  2  .  1  6  8  .  1  .  1  0  3
1  9  2  .  1  6  8  .  1  .  1  0  4
1  9  2  .  1  6  8  .  1  .  1  0  5
1  9  2  .  1  6  8  .  1  .  1  0  6
1  9  2  .  1  6  8  .  1  .  1  0  7
1  9  2  .  1  6  8  .  1  .  1  0  8
1  9  2  .  1  6  8  .  1  .  1  0  9
1  9  2  .  1  6  8  .  1  .  1  1  0
1  9  2  .  1  6  8  .  1  .  1  1  1
1  9  2  .  1  6  8  .  1  .  1  1  2
1  9  2  .  1  6  8  .  1  .  1  1  3
1  9  2  .  1  6  8  .  1  .  1  1  4
1  9  2  .  1  6  8  .  1  .  1  1  5
1  9  2  .  1  6  8  .  1  .  1  1  6
1  9  2  .  1  6  8  .  1  .  1  1  7
1  9  2  .  1  6  8  .  1  .  1  1  8
1  9  2  .  1  6  8  .  1  .  1  1  9
1  9  2  .  1  6  8  .  1  .  1  2  0
1  9  2  .  1  6  8  .  1  .  1  2  1
1  9  2  .  1  6  8  .  1  .  1  2  2
1  9  2  .  1  6  8  .  1  .  1  2  3
1  9  2  .  1  6  8  .  1  .  1  2  4
1  9  2  .  1  6  8  .  1  .  1  2  5
1  9  2  .  1  6  8  .  1  .  1  2  6
1  9  2  .  1  6  8  .  1  .  1  2  7
1  9  2  .  1  6  8  .  1  .  1  2  8
1  9  2  .  1  6  8  .  1  .  1  2  9
1  9  2  .  1  6  8  .  1  .  1  3  0
1  9  2  .  1  6  8  .  1  .  1  3  1
1  9  2  .  1  6  8  .  1  .  1  3  2
1  9  2  .  1  6  8  .  1  .  1  3  3
1  9  2  .  1  6  8  .  1  .  1  3  4
1  9  2  .  1  6  8  .  1  .  1  3  5
1  9  2  .  1  6  8  .  1  .  1  3  7
1  9  2  .  1  6  8  .  1  .  1  3  8
1  9  2  .  1  6  8  .  1  .  1  3  9
1  9  2  .  1  6  8  .  1  .  1  4  0
1  9  2  .  1  6  8  .  1  .  1  4  1
1  9  2  .  1  6  8  .  1  .  1  4  2
1  9  2  .  1  6  8  .  1  .  1  4  3
1  9  2  .  1  6  8  .  1  .  1  4  4
1  9  2  .  1  6  8  .  1  .  1  4  5
1  9  2  .  1  6  8  .  1  .  1  4  6
1  9  2  .  1  6  8  .  1  .  1  4  7
1  9  2  .  1  6  8  .  1  .  1  4  8
1  9  2  .  1  6  8  .  1  .  1  4  9
1  9  2  .  1  6  8  .  1  .  1  5  0
1  9  2  .  1  6  8  .  1  .  1  5  1
1  9  2  .  1  6  8  .  1  .  1  5  2
1  9  2  .  1  6  8  .  1  .  1  5  3
1  9  2  .  1  6  8  .  1  .  1  5  4
1  9  2  .  1  6  8  .  1  .  1  5  5
1  9  2  .  1  6  8  .  1  .  1  5  6
1  9  2  .  1  6  8  .  1  .  1  5  7
1  9  2  .  1  6  8  .  1  .  1  5  8
1  9  2  .  1  6  8  .  1  .  1  5  9
1  9  2  .  1  6  8  .  1  .  1  6  0
1  9  2  .  1  6  8  .  1  .  1  6  1
1  9  2  .  1  6  8  .  1  .  1  6  2
1  9  2  .  1  6  8  .  1  .  1  6  3
1  9  2  .  1  6  8  .  1  .  1  6  4
1  9  2  .  1  6  8  .  1  .  1  6  5
1  9  2  .  1  6  8  .  1  .  1  6  6
1  9  2  .  1  6  8  .  1  .  1  6  7
1  9  2  .  1  6  8  .  1  .  1  6  8
1  9  2  .  1  6  8  .  1  .  1  6  9
1  9  2  .  1  6  8  .  1  .  1  7  0
1  9  2  .  1  6  8  .  1  .  1  7  1
1  9  2  .  1  6  8  .  1  .  1  7  2
1  9  2  .  1  6  8  .  1  .  1  7  3
1  9  2  .  1  6  8  .  1  .  1  7  4
1  9  2  .  1  6  8  .  1  .  1  7  5
1  9  2  .  1  6  8  .  1  .  1  7  6
1  9  2  .  1  6  8  .  1  .  1  7  7
1  9  2  .  1  6  8  .  1  .  1  7  8
1  9  2  .  1  6  8  .  1  .  1  7  9
1  9  2  .  1  6  8  .  1  .  1  8  0
1  9  2  .  1  6  8  .  1  .  1  8  1
1  9  2  .  1  6  8  .  1  .  1  8  2
1  9  2  .  1  6  8  .  1  .  1  8  3
1  9  2  .  1  6  8  .  1  .  1  8  4
1  9  2  .  1  6  8  .  1  .  1  8  5
1  9  2  .  1  6  8  .  1  .  1  8  6
1  9  2  .  1  6  8  .  1  .  1  8  7
1  9  2  .  1  6  8  .  1  .  1  8  8
1  9  2  .  1  6  8  .  1  .  1  8  9
1  9  2  .  1  6  8  .  1  .  1  9  0
1  9  2  .  1  6  8  .  1  .  1  9  1
1  9  2  .  1  6  8  .  1  .  1  9  2
1  9  2  .  1  6  8  .  1  .  1  9  3
1  9  2  .  1  6  8  .  1  .  1  9  4
1  9  2  .  1  6  8  .  1  .  1  9  5
1  9  2  .  1  6  8  .  1  .  1  9  6
1  9  2  .  1  6  8  .  1  .  1  9  7
1  9  2  .  1  6  8  .  1  .  1  9  8
1  9  2  .  1  6  8  .  1  .  2  0  0
1  9  2  .  1  6  8  .  1  .  2  0  1
1  9  2  .  1  6  8  .  1  .  2  0  2
1  9  2  .  1  6  8  .  1  .  2  0  3
1  9  2  .  1  6  8  .  1  .  2  0  4
1  9  2  .  1  6  8  .  1  .  2  0  5
1  9  2  .  1  6  8  .  1  .  2  0  6
1  9  2  .  1  6  8  .  1  .  2  0  7
1  9  2  .  1  6  8  .  1  .  2  0  8
1  9  2  .  1  6  8  .  1  .  2  0  9
1  9  2  .  1  6  8  .  1  .  2  1  0
1  9  2  .  1  6  8  .  1  .  2  1  1
1  9  2  .  1  6  8  .  1  .  2  1  2
1  9  2  .  1  6  8  .  1  .  2  1  3
1  9  2  .  1  6  8  .  1  .  2  1  4
1  9  2  .  1  6  8  .  1  .  2  1  5
1  9  2  .  1  6  8  .  1  .  2  1  6
1  9  2  .  1  6  8  .  1  .  2  1  7
1  9  2  .  1  6  8  .  1  .  2  1  8
1  9  2  .  1  6  8  .  1  .  2  1  9
1  9  2  .  1  6  8  .  1  .  2  2  0
1  9  2  .  1  6  8  .  1  .  2  2  1
1  9  2  .  1  6  8  .  1  .  2  2  2
1  9  2  .  1  6  8  .  1  .  2  2  3
1  9  2  .  1  6  8  .  1  .  2  2  4
1  9  2  .  1  6  8  .  1  .  2  2  5
1  9  2  .  1  6  8  .  1  .  2  2  6
1  9  2  .  1  6  8  .  1  .  2  2  7
1  9  2  .  1  6  8  .  1  .  2  2  8
1  9  2  .  1  6  8  .  1  .  2  2  9
1  9  2  .  1  6  8  .  1  .  2  3  0
1  9  2  .  1  6  8  .  1  .  2  3  1
1  9  2  .  1  6  8  .  1  .  2  3  2
1  9  2  .  1  6  8  .  1  .  2  3  3
1  9  2  .  1  6  8  .  1  .  2  3  4
1  9  2  .  1  6  8  .  1  .  2  3  5
1  9  2  .  1  6  8  .  1  .  2  3  6
1  9  2  .  1  6  8  .  1  .  2  3  7
1  9  2  .  1  6  8  .  1  .  2  3  8
1  9  2  .  1  6  8  .  1  .  2  3  9
1  9  2  .  1  6  8  .  1  .  2  4  0
-  -  -  -  -  -  -  -  -  -  -  -  -
(venv) user1@ubuntu:~/Desktop/chat/Lesson_9$ 
"""