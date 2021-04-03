# https://leetcode.com/problems/goal-parser-interpretation/submissions/

class Solution:
    def interpret(self, command: str) -> str:
        # return command.replace("(al)", 'al').replace("()", "o")

        sol = []

        index = 0

        while index < len(command):
            if command[index] == 'G':
                sol.append('G')
                index += 1
            elif command[index] == '(':
                if command[index + 1] == ')':
                    sol.append('o')
                    index += 2
                else:
                    sol.append('al')
                    index += 4

        return "".join(sol)