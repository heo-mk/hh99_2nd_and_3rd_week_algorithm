# 입력하는 문자수
N = int(input())

for i in range(N):  # N번만큼 단어 검사 시행
    word = input()
    # 단어 왼쪽부터 오른쪽으로 가면서 검사한다.
    for index in range(len(word)-1): # 마지막 글자는 앞부분과 검사하므로 len(word) - 1
        # 2가지 경우 : 앞글자와 뒷글자가 같다, 앞글자와 뒷글자가 다르다.
        # 앞글자와 뒷글자가 다를 경우만 체크해주면 된다.
        if word[index] != word[index + 1]:
            if word[i] in word[i+1:]:
                N -= 1
                break

print(N)
