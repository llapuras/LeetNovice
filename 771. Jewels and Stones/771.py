class Solution:
    def numJewelsInStones(self, J, S):
        return len([s for s in S if s in J])