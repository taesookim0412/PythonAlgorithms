import collections
import numpy as np
from typing import List

#Runtime: 20 ms, faster than 99.56% of Python3 online submissions for Reorganize String.
#Memory Usage: 14.3 MB, less than 5.18% of Python3 online submissions for Reorganize String.

class Solution:
    def reorganizeString(self, S: str) -> str:
        wordCt = collections.Counter(S)
        res = ['' for _ in range(len(S))]
        words = list(sorted([[letter, i] for letter, i in wordCt.items()], key=lambda x: x[1]))
        indx = 0
        if words[-1][1] > (len(S) + 1 ) // 2:
            return ''
        while words:
            letter, ct = words.pop()
            for _ in range(ct):
                res[indx] = letter
                indx += 2
                if indx >= len(S):
                    indx = 1
        return ''.join(res)
    #"hehehehehehehehehehehehehehehehehehehehehehehehehehehehmecmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmvcnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvyayayayayayayayayayayayayayayayayayayayayayakfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfwfuwuwuwuwuwuwuwuwuwuwuwuwuwuwuwuwuwuwuwuwpspspspspspspspspspspspspspspspspspsxsrxrxrxrxrxrxrxrxrxrxrxrxrxrxrxrxrxgrogogogogogogogogogogogogogogogogiobibibibibibibibibibibibibibibitbdtdtdtdtdtdtdtdtdtdtdtdtdtdtdtqzqzqzqzqzqzqzqzqzqzqzjzjzjzljljljljljljljljlll"
    #('lll')
    #PROBLEM: The solution revolves around the fact that if there is a solution, then the most occuring character will be every other character.
    #This is the base case for deriving a solution.
    #Instead of iterating each letter and appending to the resultant string,
    #the answer is to iterate through the resultant string (i*2) % len and pop each letter.
    def reorganizeString2(self, S: str) -> str:
        wordCt = collections.Counter(S)
        res = ['' for _ in range(len(S))]
        words = list(sorted([[letter, i] for letter, i in wordCt.items()], key=lambda x: x[1]))
        indx = 0
        offset = 0
        if words[-1][1] > (len(S) + 1 ) // 2:
            return ''
        while indx != len(S):
            offset -= 1
            if indx % 2:
                offset += 2
            print(offset)
            words[offset][1] -= 1
            nextLetter = words[offset][0]
            if words[offset][1] == 0:
                words.pop(offset)
            res[indx] = nextLetter
            indx += 1
        return ''.join(res)



#61/62
# Wrong Answer
# Details
# Input
# "tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao"
# Output
# ""
# Expected
# "eweweweweweweweweweweweweweueueueueueueueueueueueueueueuhuhuh
class Solution2:
    def reorganizeString(self, S: str) -> str:
        wordCt = collections.Counter(S)
        print(len(wordCt.keys()), len(S))
        res = ['' for _ in range(len(S))]
        words = list(sorted([[letter, i] for letter, i in wordCt.items()], key=lambda x: x[1]))
        print(words)
        indx = 0
        prevLetter = ''
        while indx != len(S):
            offset = -1
            if indx % 2:
                if len(words) > 1:
                    offset -= 1
            words[offset][1] -= 1
            nextLetter = words[offset][0]
            if nextLetter == prevLetter:
                return ''
            if words[offset][1] == 0:
                words.pop(offset)
            res[indx] = nextLetter
            prevLetter = nextLetter
            indx += 1

        return ''.join(res)


#class Solution:
    #abcaa
    # def reorganizeString(self, S: str) -> str:
    #     wordCt = collections.Counter(S)
    #     if len(wordCt)  <= len(S) / 2:
    #         return ''
    #     res = ['' for _ in range(len(S))]
    #     indx = 0
    #     while indx != len(S):
    #         dels = []
    #         for word, ct in wordCt.items():
    #             res[indx] = word
    #             if ct == 1:
    #                 dels += word
    #             else:
    #                 wordCt[word] -= 1
    #             indx += 1
    #             if indx == len(S):
    #                 break
    #         for entry in dels:
    #             del wordCt[entry]
    #     return ''.join(res)



s = Solution()
print(s.reorganizeString("aab"))
print(s.reorganizeString("aaab"))
print(s.reorganizeString("aaabc"))
print(s.reorganizeString("abracadabra"))
print(s.reorganizeString("patch"))
print(s.reorganizeString("tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao"))
print(s.reorganizeString2("tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao"))