# 열린 괄호만 저장하고, 닫힌 괄호가 나오면 열린 괄호 없애기. stack을 이용한다.
# 그 과정을 해주는 함수
def is_balanced_world(string):
    st = []   # stack

    for s in string:
        # 열린 괄호만 저장하기 
        if s == '(' or s == '[': 
            st.append(s)
        
        # 닫힌 괄호가 나올때, 괄호가 ) ] 두 종류이므로 stack에 있는 열린 괄호들과 비교해 균형이 맞는지 확인한다
        elif s == ')' or s == ']':
            # stack 안에 열린 괄호가 이미 닫힌 괄호와 만나 없어졌거나 애초에 열린 괄호가 없는 경우.
            if len(st) == 0:
                return False
            
            popped = st.pop()
            if s == ')' and popped == '(': # ()의 균형이 확인됨.
                continue
            elif s == ']' and popped == '[': # ()의 균형이 확인됨.
                continue
            else:
                return False

        # 괄호가 모두 짝이 맞아 stack이 비어 있다 == '균형있는 문자열'.    
    if len(st) == 0:
        return True
    else:
        return False

while True:
    sentence = input()
    if sentence == ".":
        break
    
    # 균형있는 문자열로 판정되면 'yes' 출력, 아니면 'no' 출력
    is_balanced = is_balanced_world(sentence)
    if is_balanced == True:
        print('yes')
    else:
        print('no')