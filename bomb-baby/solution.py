def solve(x, y):
    if x==1 and y==1:
        return 0
    elif x==0 or y==0:
        return float('inf')

    n_times = int(max(x, y)/min(x, y))

    if (n_times>=2) and not (x==1 or y==1):
        if y>x:
            y = y - (x*n_times)
        else:
            x = x - (y*n_times)

        return solve(x, y) + n_times

    if y>x:
        y = y - x
    else:
        x = x - y

    return solve(x, y) + 1



def solution(x, y):
    x = int(x)
    y = int(y)

    solution = solve(x, y)

    if solution==float('inf'):
        solution = 'impossible'

    return str(solution)


if __name__ == "__main__":
    assert solution('2', '1') == '1'
    assert solution('4', '7') == '4'
