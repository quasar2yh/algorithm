// # A 강조하기
// 문자열 myString이 주어집니다. 
// myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, 
// "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 
// return 하는 solution 함수를 완성하세요.

function solution(myString) {
    let modifiedStr = myString.toLowerCase()
    modifiedStr = modifiedStr.replaceAll("a", "A")
    return modifiedStr
}

// 화살표 함수를 조금 더 적극적으로 이용해보자.
const solution=s=>s.toLowerCase().replaceAll('a','A');
