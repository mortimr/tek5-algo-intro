#! /bin/python3

import numpy
import math
import time

# log(n)
def get_center_index(list, begin_idx, end_idx, val):
    if (begin_idx == end_idx):
        return begin_idx
    center = math.floor((end_idx - begin_idx) / 2) + begin_idx
    if (list[center] > val):
        return get_center_index(list, begin_idx, center, val)
    return get_center_index(list, center + 1, end_idx, val)

def parcours(list):
    return list

def get_score(list):
    ret = 0
    pos = 0
    while len(list) != 0:
        dest = list[0]
        remaining = list[1:]
        distance = numpy.abs(dest - pos)
        ret += distance * (len(remaining) + 1)
        pos = dest
        list = remaining
    return ret

def parcours(list):
    plowpos = 0
    sorted_list = numpy.sort(list, kind='mergesort') # => n * log(n)
    ret_list = []
    while (len(sorted_list) != 0): # 2 to n loop rounds, so => n
        center_idx = get_center_index(sorted_list, 0, len(sorted_list), plowpos) # log(n)
        left_idx = 0
        right_idx = len(sorted_list) - 1
        left_count = center_idx;
        right_count = len(sorted_list) - center_idx

        # loop runs up to n - 1 times 
        while (sorted_list[left_idx] < plowpos and sorted_list[right_idx] > plowpos):
            leftmost = numpy.abs(sorted_list[left_idx])
            left_score = (right_count * leftmost) / left_count

            rightmost = numpy.abs(sorted_list[right_idx])
            right_score = (left_count * rightmost) / right_count

            #print(left_idx, left_score, right_idx, right_score)

            if (left_score < right_score):
                right_idx -= 1
                right_count -= 1
            else:
                left_idx += 1
                left_count -= 1

        if (sorted_list[left_idx] >= plowpos):
            ret_list = [*ret_list, *sorted_list[center_idx: right_idx + 1]]
            plowpos = sorted_list[right_idx]
            sorted_list = [*sorted_list[0: center_idx], *sorted_list[right_idx + 1:]]
        else:
            ret_list = [*ret_list, *numpy.flip(sorted_list[left_idx: center_idx])]
            plowpos = sorted_list[left_idx]
            sorted_list = [*sorted_list[0: left_idx] , *sorted_list[center_idx:]]
            
    return ret_list

def parcours_greedy(list):
    ret = []
    snowplow_pos = 0
    arr = numpy.asarray(list)
    while (len(arr) != 0):
        idx = numpy.abs(arr - snowplow_pos).argmin()
        ret.append(arr[idx])
        snowplow_pos = arr[idx]
        arr = numpy.delete(arr, idx)
    return ret

def test_run():
    list = numpy.random.normal(0, 100000, 100000)
    print('Running Greedy')
    greedy_begin = time.time()
    greedy = parcours_greedy(list)
    greedy_time = time.time() - greedy_begin
    print('Greedy Time {}'.format(greedy_time))
    greedy_score = get_score(greedy)
    print('Greedy Score {}'.format(greedy_score))
    print('Running Solution')
    sol_begin = time.time()
    sol = parcours(list)
    sol_time = time.time() - sol_begin
    print('Solution Time {}'.format(sol_time))
    sol_score = get_score(sol)
    print('Solution Score {}'.format(sol_score))
    print('Speedup: {}'.format(greedy_time / sol_time))
    print('Efficiency: {}'.format(greedy_score / sol_score))


if __name__ == '__main__':
    test_run()