#!/usr/bin/env python3
# R = 2 # 设置个让程序可以无限次输入数字的条件，配合第一个while使用
while True: # 可以无限次输入待转换数字
# while R >1: # 对应第二行
    N = 0 #用来记录number能被2整除的次数
    sum =0 # 记录结果
    print('please enter a number or enter 0 to esc') # 提示用户输入数字或退出
    number = int(input()) # 存储输入
    if number == 0: # 用来允许用户退出转换程序
        break
    num = number # 将输入分两份处理，一是求整，作为十进制的幂，二是求余，作为10进制的项
    while number >= 2: # 求最高次幂
        number = number // 2
        N+=1
    m = N #存两份最高幂，将余数倒过来
    while num >= 1: #求余求和转换
        sum = sum + (num % 2) * (10**(m - N)) #转换
        num = num // 2
        N = N -1 # 降幂
    print('Binary system is {}'.format(sum)) #输出转换好的十进制


