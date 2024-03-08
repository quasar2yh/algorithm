'''
홀짝 구분하기
제출 내역
문제 설명
자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.
'''
a = int(input())
res = 'even' if a%2 == 0 else 'odd'
print(f'{a} is {res}')