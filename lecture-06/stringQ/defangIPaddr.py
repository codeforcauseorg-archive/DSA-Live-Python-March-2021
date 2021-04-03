class Solution:
    def defangIPaddr(self, address: str) -> str:
        #         sol = []

        #         for ch in address:
        #             if ch == ".":
        #                 sol.append("[.]")
        #             else:
        #                 sol.append(ch)

        #         return "".join(sol)

        return address.replace(".", "[.]")


