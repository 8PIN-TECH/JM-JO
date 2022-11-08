def hanoi():
    num = int(input('숫자를 입력 하여 주세요.'))
    if 1 <= num <= 100:
        print(2 ** num-1)
        hanoi_star(num, 1, 3, 2)
    else:
        print("1 ~ 100 사이의 숫자만 입력 하여 주세요.")


def hanoi_star(num, from_pos, to_pos, temp_pos):
    if num == 1:
        print(from_pos, to_pos)
        return
    hanoi_star(num - 1, from_pos, temp_pos, to_pos)
    print(from_pos, to_pos)
    hanoi_star(num - 1, temp_pos, to_pos, from_pos)


if __name__ == '__main__':
    hanoi()
