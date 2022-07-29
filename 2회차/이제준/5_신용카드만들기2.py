import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

lst = []
for i in range(1, T + 1):
    nums = (str(input()))
    nums = list(nums.replace('-',''))
    # 만약 주어진 카드 번호에 '-' 가 있으면 .replace('-', '') 통해
    # '-'를 없애기

    lst = []
    if nums[0] == '3' or nums[0] == '4' or nums[0] == '5' or nums[0] == '6' or nums[0] == '9':
        lst.append(nums)
    # 숫자가 3, 4, 5, 6, 9로 시작하면 리스트에 넣어주고
    else:
        print(f'#{i} 0')
    # 그게 아니면 바로 0으로 출력한다

    # 리스트 안에 리스트가 있어서, 리스트 하나를 for 문을 통해 없애고
    # len()을 통해 리스트 안에 숫자들을 센 후
    # 값이 16이면 1을 아니면 0을 출력한다
    for valid in lst:
        if len(valid) == 16:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')