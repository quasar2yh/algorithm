function solution(my_string, alp) {
  let regex = new RegExp(alp.toLowerCase(), "g");
  modified_string = my_string.replace(regex, alp.toUpperCase());
  return modified_string;
}

// replaceAll 등장
function solution2(my_string, alp) {
  return my_string.replaceAll(alp.toLowerCase(), alp.toUpperCase());
}

console.log(solution2("programmersp", "p"));
