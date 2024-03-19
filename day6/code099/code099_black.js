// # 부분 문자열 이어 붙여 문자열 만들기

// 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. 
// parts[i]는 [s, e] 형태로, 
// my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 
// 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 
// 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

function solution(my_strings, parts) {
    let subStr = ""
    for (let i=0; i<my_strings.length; i++){
        subStr += my_strings[i].substring(parts[i][0], parts[i][1]+1)
    }
    return subStr
}


// 배열은 map 함수 활용하는 법 익히자
// map의 첫번째 인자는 배열의 요소인데, 요소가 [0,4]와 같은 배열 이므로 이것을 인자로 [s, e]로 표현
function solution(my_strings, parts) {
    return parts.map(([s, e], i) => {
        return my_strings[i].slice(s, e + 1)
    }).join('')
}
