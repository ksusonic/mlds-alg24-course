def solution(line: str) -> int:
    res = line.count("B")
    line = line.replace("B", "")

    cur_side = "L"
    for i in range(len(line)):
        if line[i] != cur_side:
            continue

        if (i + 1 < len(line) and line[i] == line[i + 1]) or (
            i + 1 == len(line) and line[i] == "L"
        ):
            cur_side = "R" if cur_side == "L" else "L"

        res += 1

    if cur_side != "R":
        res += 1

    return res


if __name__ == "__main__":
    line = input()
    print(solution(line))
