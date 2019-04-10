import math, numpy
def work(students):
    bestStudent  = students[0]
    hours = 0
    for i in students[1:]:
        hours += bestStudent - i
    return hours

def solution():
    n, p = list(map(int, input().split()))
    students = input().split()
    students = list(map(int, students))

    elements = numpy.array(students)

    mean = numpy.mean(elements, axis=0)
    sd = numpy.std(elements, axis=0)

    final_list = [x for x in students if (x > mean - 1 * sd)]
    print(final_list)
    final_list = [x for x in final_list if (x < mean + 1 * sd)]
    print(final_list)
   
    if p == 0 or n == 0: 
        return 0

    bestRange = math.inf
    bestStudent = 0
    leastAmount = math.inf
    for i in range(0, (n - p + 1)):   
        subStudents = students[i:i+p]
        currentAmount = work(subStudents)
        if currentAmount < leastAmount:
            leastAmount = currentAmount
            bestStudent = i
   
    return leastAmount

for i in range(eval(input())):
    print('Case #%d: %d' % (i+1, solution()))