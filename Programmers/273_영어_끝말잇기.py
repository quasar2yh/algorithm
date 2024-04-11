"""
1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.

1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
이전에 등장했던 단어는 사용할 수 없습니다.
한 글자인 단어는 인정되지 않습니다.
다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.

tank → kick → know → wheel → land → dream → mother → robot → tank

위 끝말잇기는 다음과 같이 진행됩니다.

1번 사람이 자신의 첫 번째 차례에 tank를 말합니다.
2번 사람이 자신의 첫 번째 차례에 kick을 말합니다.
3번 사람이 자신의 첫 번째 차례에 know를 말합니다.
1번 사람이 자신의 두 번째 차례에 wheel을 말합니다.
(계속 진행)
끝말잇기를 계속 진행해 나가다 보면, 3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.

사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.

제한 사항
끝말잇기에 참여하는 사람의 수 n은 2 이상 10 이하의 자연수입니다.
words는 끝말잇기에 사용한 단어들이 순서대로 들어있는 배열이며, 길이는 n 이상 100 이하입니다.
단어의 길이는 2 이상 50 이하입니다.
모든 단어는 알파벳 소문자로만 이루어져 있습니다.
끝말잇기에 사용되는 단어의 뜻(의미)은 신경 쓰지 않으셔도 됩니다.
정답은 [ 번호, 차례 ] 형태로 return 해주세요.
만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0]을 return 해주세요.

"""
import math
# 중복된 단어 때문에 끝말잇기가 끝날수도 있고 잘못된 단어 때문에 끝말잇기가 끝날 수도 있다.
# 두 경우 모두 해당하더라도 먼저 나온 경우에 의해서 게임이 종료된다.


def solution(n, words):
    # 끝말잇기를 잘못한 경우
    whereis1 = 0
    answer1 = [0, 0]
    whereis2 = 0
    answer2 = [0, 0]
    for idx in range(len(words)-1):
        if words[idx][-1] != words[idx+1][0]:
            whereis1 = idx+2
            answer1 = [(whereis1) % n if (whereis1) %
                       n != 0 else n, math.ceil((whereis1)/n)]
            break
    # 중복 단어 찾기
    set_words = set(words)
    whereis2_dic = {}
    if len(set_words) != len(words):
        # 중복 된 게 2개 이상인 경우, 첫번째 나온 중복을 찾아야 함
        for word in words:
            if words.count(word) > 1:
                # 중복된 단어의 위치
                whereis2 = words.index(word, words.index(word)+1)+1
                answer2 = [whereis2 % n if whereis2 %
                           n != 0 else n, math.ceil(whereis2/n)]
                whereis2_dic[whereis2] = answer2
        first_dup = sorted(whereis2_dic.items())[0]
        whereis2 = first_dup[0]
        answer2 = first_dup[1]
    if whereis1 and whereis2:
        return answer1 if whereis1 < whereis2 else answer2
    elif not whereis1 and not whereis2:
        return [0, 0]
    elif not whereis1:
        return answer2
    elif not whereis2:
        return answer1
    else:
        return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel",
      "land", "dream", "mother", "robot", "tank"]))


# 다 찾고 빠른거 고르는 게 아니라, 처음부터 있는지 체크
# 생각을 잘못 시작하면 오래 걸림....
def solution(n, words):
    answer = []
    turn = 0
    wordList = [words[0]]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for idx in range(1, len(words)):
        if words[idx-1][-1] != words[idx][0]:
            turn = idx
            break
        if words[idx] in wordList:
            turn = idx
            break
        wordList.append(words[idx])
    answer = [turn%n +1, turn//n + 1]
    if turn == 0:
        answer = [0, 0]
    return answer