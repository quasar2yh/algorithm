// https://school.programmers.co.kr/learn/courses/30/lessons/120850?language=python3

// 문자열 my_string이 매개변수로 주어질 때,
// my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를
// return 하도록 solution 함수를 작성해보세요.

// 제한사항
//     1 ≤ my_string의 길이 ≤ 100
//     my_string에는 숫자가 한 개 이상 포함되어 있습니다.
//     my_string은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다. - - -

// 입출력 예 #1

// "hi12392"에 있는 숫자 1, 2, 3, 9, 2를
// 오름차순 정렬한 [1, 2, 2, 3, 9]를 return 합니다.

// js는 정규표현식을 사용하는 게 편하다...
//js의 split 함수는 '' 따옴표를 써줘야 한다.
function solution(my_string) {
  return my_string.replace(/\D/g, "").split('').map(v=>+v).sort();
}

console.log(solution("abcde0"))

// function solution(my_string) {
//     return Array.from(my_string).filter(v => !isNaN(+v)).sort((a,b) => a - b).map(v => +v);
// }

// function solution(my_string) {
//     return my_string
//       .split("")
//       .filter((char) => !isNaN(char))
//       .map((number) => parseInt(number))
//       .sort((a, b) => a - b);
//   }

// function solution(my_string) {
//     return my_string.replace(/[^\d]/g,'').split('').map(v=>+v).sort();
// }

// function solution(my_string) {
//     return my_string.split("").filter((v) => !isNaN(v)).map((v) => v*1).sort((a,b) => a-b)
// }

// function solution(my_string) {
//     return my_string.match(/\d/g).sort((a, b) => a - b).map(n => Number(n));
// }
