# 24조 강상연의 코드
# 균형있는 문자열인지에 대한 여부를 판별하는 함수입니다
# 문자열 내의 모든 괄호가 알맞은 짝이 있다면 True를 반환합니다
def is_balanced_string(string: str):
    brackets_stack = list()

    for char in row:
        # 여는 괄호인 경우 스택에 추가합니다
        if char == "(" or char == "[":
            brackets_stack.append(char)

        # 닫는 괄호인 경우 짝이 맞는지 확인합니다
        elif char == ")" or char == "]":
            if len(brackets_stack) == 0:
                return False

            popped = brackets_stack.pop()
            if char == ")" and popped == "(":
                print(brackets_stack)
                print()
                continue
            elif char == "]" and popped == "[":
                print(brackets_stack)
                print()
                continue
            else:
                return False
        print(brackets_stack)         
    # 괄호가 전부 짝이 맞아 스택이 모두 비었다면 "균형있는 문자열"입니다
    if len(brackets_stack) == 0:
        return True
    else:
        return False


while True:
    row = input()

    # 프로그램 종료 조건입니다
    if row == ".":
        break

    # 균형잡힌 문자열인지 확인하고, 맞다면 yes를 아니라면 no를 출력합니다
    is_balanced = is_balanced_string(row)
    if is_balanced is True:
        print("yes")
    else:
        print("no")

