// 할 일 목록

// 오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가
// 매개변수로 주어질 때, todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을
// return 하는 solution 함수를 작성해 주세요.

function solution(todo_list, finished) {
  remain_li = [];
  for (let [idx, check] of finished.entries()) {
    if (check == false) {
      remain_li.push(todo_list[idx]);
    }
  }
  return remain_li;
}

console.log(
  solution(
    ["problemsolving", "practiceguitar", "swim", "studygraph"],
    [true, false, true, false]
  )
);

// 필터 사용 적극적으로 하자
function solution(todo_list, finished) {
  var answer = [];
  return todo_list.filter((e, i) => !finished[i]);
}

//js의 not 연산자는 !
function solution(td, f) {
    var answer = [];

    for(let i = 0;i<td.length; i++){
        if(!f[i]){
            answer.push(td[i])
        }
    }

    return answer;
}