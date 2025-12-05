class Solution:
    def removeStars(self, s: str) -> str:
            answer = []
            for char in s:
                if len(answer) > 0 and char == '*':
                    answer.pop()
                else:
                    answer.append(char)
            
            return "".join(answer)
        