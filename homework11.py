def test(*args):
    print("Тест")
    print('тип args:', type(args))
    print(args)
    for i, j in enumerate(args):
        print('Параметр:', i, j)


test('Привет!', True, [20, 30, 40], {'сколько рук', 2})


def factor(n):
    if n == 0:
        return 1
    else:
        return n * factor(n - 1)


print(factor(11))