class Solution:
    def removeStars(self, s: str) -> str:
        stacks = []
        for stack in s:
            if stack == '*':
                stacks.pop()
            else:
                stacks.append(stack)

        return "".join(stacks)