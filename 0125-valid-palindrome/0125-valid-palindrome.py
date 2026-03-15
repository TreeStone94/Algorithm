class Solution:
    def isPalindrome(self, s: str) -> bool:
# 어떤 문구가 모든 대문자를 소문자로 변환하고 영숫자가 아닌 문자를 모두 제거한 후에도 앞뒤로 읽었을 때 똑같이 읽힌다면, 그 문구는 회문입니다. 영숫자에는 문자와 숫자가 포함됩니다.
# 문자열 s가 주어졌을 때, s가 회문이면 true를, 그렇지 않으면 false를 반환하십시오.

# 대문자를 소문자로 변환
        # 0~9 48~57
        # 65-90
        answer = ""
        for c in s:
            o = ord(c)
            if 65 <= o <=90:
                answer += chr(o+32)
            elif 97 <= o <= 122:
                answer += c
            elif 48 <= o <= 57:
                answer += c

        if answer == "" or answer == answer[::-1]:
            return True
        else:
            return False




# 영숫자가 아닌 문자를 모두 제거

# 앞뒤로 읽었을 때 똑같이 읽힌

