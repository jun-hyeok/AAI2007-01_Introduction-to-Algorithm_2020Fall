def job_scheduling(J):
    J.sort(key = lambda x: x[2])
    solution_set = []
    previous_f = 0
    for i in range(len(J)):
        if J[i][1] >= previous_f:
            solution_set.append(J[i])
            previous_f = J[i][2]
    return solution_set

J =   [['a', 0, 6],  ['b', 1, 4], ['c', 3, 5], 
       ['d', 3, 8], ['e', 4, 7], ['f', 5, 9],
       ['g', 6, 10], ['h', 8, 11]]
print(job_scheduling(J))



