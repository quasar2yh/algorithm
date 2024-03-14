// # 공백으로 구분하기 2


// 단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때,
// my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

function solution(my_string) {
    return my_string.split(" ").filter(char=>char!=="");
}

console.log(solution("i   love you"))

// js의 split은 자동으로 여백을 자르고 배열로 만들지 않는다.