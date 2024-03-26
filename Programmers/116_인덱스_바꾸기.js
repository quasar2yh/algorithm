// https://school.programmers.co.kr/learn/courses/30/lessons/120895?language=python3
// 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
// my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을
// return 하도록 solution 함수를 완성해보세요.

function solution(my_string, num1, num2) {
  let str_li = my_string.split("");
  let str1 = str_li[num1];
  let str2 = str_li[num2];
  str_li[num1] = str2;
  str_li[num2] = str1;
  return str_li.join("");
}

console.log(solution("I love you", 3, 6));

// 구조 분해 사용

function solution(my_string, num1, num2) {
  my_string = my_string.split("");
  [my_string[num1], my_string[num2]] = [my_string[num2], my_string[num1]];
  return my_string.join("");
}
