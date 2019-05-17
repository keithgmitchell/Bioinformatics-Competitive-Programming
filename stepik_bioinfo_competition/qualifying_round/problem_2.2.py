import csv

def solve_problem(n_next, a, b, past_n):
    for i in range(0, 10000000):
        past_n = n_next
        n_next = (n_next * a) - (b * (n_next**2))
        if n_next == past_n:
            return n_next
        elif n_next > 10**30:
            return -1
        elif n_next <= 0:
            return 0
        elif n_next <= 10**-4:
            return 0

def solve_problem_backup(n_next, a, b, past_n):
    for i in range(0, 100000000):
        past_n = n_next
        n_next = (n_next * a) - (b * (n_next**2))
        if abs(n_next-past_n) <= 10**-3:
            return ((n_next + past_n)/2)

with open('tests.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(reader, None)
    solution_list = []
    for row in reader:
        solution = solve_problem(float(row[0]), float(row[1]), float(row[2]), 0)
        if solution is None:
            solution = solve_problem_backup(float(row[0]), float(row[1]), float(row[2]), 0)
        solution_list.append(solution)
        print (solution)


# print(solve_problem(0.5,1,1,0))
# print(solve_problem(10,1,2,0))
# print(solve_problem(0.5,1.5,1,0))
# print(solve_problem(0.1,2,2,0))

# print(solve_problem(0.5,3,1,0))
# print(solve_problem(1.047,1.071,0,0))

# print (10**-3)