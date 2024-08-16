def backtrack(a, k, n):
    c = [0] * MAXCANDIDATES

    if k == n:
        process_solution(a, k)
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]