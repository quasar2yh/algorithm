// 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다.
// 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록
// solution 함수를 완성해주세요.

function solution(i, j, k) {
    let str = Array(j - i + 1).fill(i).map((v, i) => v + i).join('')
    return Array.from(str).filter(n => +n===k).length
}

console.log(solution(1, 13, 1))  // [ 5, 6, 7, 8, 9 ]

//js에서는 리스트 컴프리헨션과 range()를 합쳐서 사용하는 방법이 없음 -> Array(), fill(), map() 활용
//js에서는 count을 셀 때 필터링 이후 length 하는 게 더 편할 수도 있음
