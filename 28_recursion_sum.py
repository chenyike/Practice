def recursive_sum(lst):
    # base-case  - simple input for which answer is immediate
    if len(lst) == 0
    return 0
    first = lst[0]
    sum_rem = recursive_sum(lst[1:])
    return first + sum_rem
