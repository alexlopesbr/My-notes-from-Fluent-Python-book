# 02.18 | 73 | Given the score on an exam,
# grid returns the corresponding grade in the form of a letter

import bisect

brearkpoints = [60, 70, 80, 90]
grades = 'FDCBA'
scores = [33, 99, 77, 70, 89, 90, 100, 59]


def grade(score, brearkpoints, grades):
    i = bisect.bisect(brearkpoints, score)
    return grades[i]


grade_values = [grade(score, brearkpoints, grades) for score in scores]

print(grade_values)

# ======

list_test = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

c_left = bisect.bisect_left(list_test, 'c')
c_right = bisect.bisect_right(list_test, 'c')

# print(c_left)
# print(c_right)
