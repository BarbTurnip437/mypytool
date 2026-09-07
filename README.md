# mypytool
一个有许多功能的python库
（由于本人十一岁能力有限，代码水平不高请谅解）

## 安装方法

pip install mypytool

## 功能介绍

### main.py

perfect_square_plus_gs 功能：完全平方和公式

perfect_square_plus_z 功能：完全平方和值

perfect_square_sub_gs 功能：完全平方差公式

perfect_square_sub_z 功能：完全平方差值

glm 功能：十进制转格雷码

glm2bin 功能：格雷码转二进制

glm2dex 功能：格雷码转十进制

base_conversion 功能：进制转换将十进制x转换成y进制

base_conversion 功能：进制转换将二进制str x转换成十进制

factorial_recursion 功能：阶乘

fibonacci_recursion 功能：求斐波那契的第n项值

### date.py

month_first_day 功能：求当前月第一天的星期

month_length 功能：求月份天数

### linked_list.py

class GeneralLinkedList 功能：单向链表

class CycleLinkedList 功能：循环链表

### graghic.py

class Circle 功能：圆

class Square 功能：正方形

class Rectangle 功能：长方形

class Triangle 功能：三角形

class Parallelogram 功能：平行四边形

class Trapezoid 功能：梯形

## 更新日志

- 0.2
  - main.py
    - 移除了 fast_pow 和 pow，请使用 ** 或 math.pow
    - 移除了 swap, swap1 和 swap2
  - date.py
    - 移除了 leap_year，请使用 calendar.isleap
    - 重命名 month_day -> month_length，并且现在这个函数不再具有默认值
  - linked_list.py
    - 重命名 General_Linked_list -> GeneralLinkedList
    - 重命名 Cycle_Linked_list -> CycleLinkedList
  - graghic.py
    - 更新了 graghic.py 的内部实现，变化较大
  - 移除了整个 stack.py，请使用列表
  - 移除了整个 queue.py，请使用 queue.Queue
  - 移除了整个 sort.py，请使用 sorted
