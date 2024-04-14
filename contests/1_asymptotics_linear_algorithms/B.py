def main(l: list):
    ones = 0
    twos = 0

    for num in l:
        # Добавляем num к twos, если он уже был в ones
        twos |= ones & num
        # Добавляем num к ones
        ones ^= num
        # Если ones и twos оба имеют бит в одной позиции
        # этот бит должен быть сброшен, так как число появилось 3 раза
        threes = ones & twos
        ones &= ~threes
        twos &= ~threes
    return (ones, 1) if ones else (twos, 2)


if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    res = main(l)
    print(*res)
