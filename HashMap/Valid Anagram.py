class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1={}
        freq2={}

        for i in s:
            if i in freq1:
                freq1[i]=freq1[i]+1

            freq1[i]=1

        for j in t:
            if j in freq2:
                freq2[j]=freq2[j]+1

            freq2[j]=1

        if freq1 == freq2:
             return True
        else:
            return False
        