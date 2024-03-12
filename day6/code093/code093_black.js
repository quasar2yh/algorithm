// 문자열 바꿔서 찾기

// 문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다.
// myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중
// pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.

function solution(myString, pat) {
  let replacedAb = "";
  for (let char of pat) {
    if (char === "A") {
      replacedAb += "B";
    } else if (char === "B") {
      replacedAb += "A";
    }
  }
  if (myString.includes(replacedAb)) {
    return 1;
  } else {
    return 0;
  }
}

// 우수풀이

const solution = (myString, pat) =>
  [...myString]
    .map((v) => (v === "A" ? "B" : "A"))
    .join("")
    .includes(pat)
    ? 1
    : 0;

function solution(str, pat) {
  pat = pat.replaceAll("A", "X").replaceAll("B", "A").replaceAll("X", "B");

  return str.indexOf(pat) === -1 ? 0 : 1;
}
