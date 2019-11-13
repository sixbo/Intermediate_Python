class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j=set(J)
        s=set(S)

        w=(j&s)
        o=s-w
        listo=list(o)
        lists=list(S)
        count=0
        for i in range(len(listo)):
            for j in range(len(lists)):
                if listo[i]==lists[j]:
                    count=count+1
        return(len(lists)-count)