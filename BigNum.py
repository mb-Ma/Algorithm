# _*_coding: utf-8 _*_
# author    :西南交一枝花
# DATA  : 13:41
# LAST MODIFIED BY :西南交一枝花
# LAST MODIFIED BY  : 13:41

def add(s1, s2):
    sum_list = [0] * (len(s1) + 1)
    result = ''
    for i in range(len(s1)-1, -1, -1):
        v_add = int(s1[i]) + int(s2[i]) + sum_list[i]
        if v_add > 9:
            sum_list[i - 1] = 1
            v_add -= 10
        result = str(v_add) + result
    print(str(result))

s1 = '12332453'
s2 = '328378237283'

if len(s1) < len(s2):
    s1 = '0'*(len(s2)-len(s1)) + s1
else:
    s2 = '0' * (len(s1) - len(s2)) + s2

add(s1, s2)