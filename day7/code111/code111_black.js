// # 최댓값 만들기 (2)

// """
// 정수 배열 numbers가 매개변수로 주어집니다.
// numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록
// solution 함수를 완성해주세요.
// """

function solution(numbers) {
  numbers.sort();
  return Math.max(
    numbers[0] * numbers[1],
    numbers[numbers.length - 1] * numbers[numbers.length - 2]
  );
}
// 자바스크립트는 음수 인덱싱이 없다!!!
console.log(solution([1, 2, -3, 4, -5]));
