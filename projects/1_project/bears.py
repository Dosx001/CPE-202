def bears(n):
    try:
        m = 0
        for i in n:
            m += 1
    except TypeError:
        if n == 42:
            return True
        if n < 42:
            return False
        m = 1
        n = [n]
    y = []
    for i in range(len(n)):
        if n[i] % 2 == 0:
            n.append(n[i] // 2)
        if n[i] % 3 == 0 or n[i] % 4 == 0:
            nums = list(str(n[i]))
            if nums[-2] != '0' and nums[-1] != '0':
                n.append(n[i] - int(nums[-2]) * int(nums[-1]))
        if n[i] % 5 == 0:
            n.append(n[i] - 42)
    for i in range(m):
        n.pop(0)
    for i in n:
        if i < 42:
            y.append(i)
    for i in y:
        n.remove(i)
    if len(n) == 0:
        return False
    if 42 in n:
        return True
    return bears(n)
