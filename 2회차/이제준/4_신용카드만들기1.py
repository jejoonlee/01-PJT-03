import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for t in range(1, T + 1):
    num = map(int, input().split())
    nums = list(num)
    # 숫자들을 정수로 변환한 후 리스트에 넣는다

    # index가 홀수면 2를 곱하고 더하는 거지만,
    # 인덱스는 0으로 시작해서
    # 반대로 짝수면 2를 곱하고,
    # 홀수면 그냥 더하기로 했다
    result = 0
    for i in range(len(nums)):
        if (i) % 2 == 1:
            result += nums[i]
        else:
            result += (nums[i] * 2)
    
    # 그리고 10으로 나눈 후 나눠 떨어지면 0을 출력하고
    # 그 외에는 10을 나눠 떨어진 숫자에 빼서,
    # 그 숫자를 출력했다
    if result % 10 == 0:
        print(f'#{t} 0')
    else:
        print(f'#{t} {10 - result % 10}')