// 정수 n이 매개변수로 주어질 때,
// 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.

// arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.

function solution(n) {
  var answer = [];
  for (let i = 0; i < n; i++) {
    let inner_arr = [];
    for (let j = 0; j < n; j++) {
      inner_arr.push(i === j ? 1 : 0);
    }
    answer.push(inner_arr);
  }
  return answer;
}
console.log(solution(3));


// 우수 답변
function solution(n) {
  const answer = Array.from(Array(n), () => Array(n).fill(0));

  for (let i = 0; i < n; i++) {
    answer[i][i] = 1;
  }

  return answer;
}

function solution(n) {
  return Array(n)
    .fill()
    .map((_, i) =>
      Array(n)
        .fill()
        .map(($, j) => (i === j ? 1 : 0))
    );
}
