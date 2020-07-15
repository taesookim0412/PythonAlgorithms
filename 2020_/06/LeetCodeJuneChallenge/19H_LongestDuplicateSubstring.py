#Binary Search
#Rabin Karp
#7 / 16 test cases passed.
class Solution2:
    def longestDupSubstring(self, S: str) -> str:
        def test(L):
            h = 0
            a = (26 ** mid) % (2**63-1)
            for i in range(L):
                h = (h * 26 + elems[i]) % (2**63 - 1)
            hashes = {h}
            #n-mid+1
            for i in range(1,n-mid+1):
                #some kinda hash
                h = (h * 26 - elems[i-1] * a + elems[i+mid-1]) % (2**63 - 1)
                if h in hashes:
                    print(h, i)
                    return i
                hashes.add(h)
            return -1

        elems = [ord(x) - ord('a') for x in S]
        n = len(S)
        l = 0
        r = n
        res = -1
        while l < r:
            mid = l+(r-l)//2
            query = test(mid)
            if query != -1:
                l = mid + 1
                res = query
            else:
                r = mid - 1
        print(res)
        return S[res:res+l-1]


#Accepted solution
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def rabin_karp(m):
            h = 0
            d = 26
            for i in range(m):
                h = (h * d + asc[i]) % q

            a = pow(d, m, q)
            lookup = {h}
            for i in range(1, n - m + 1):
                h = (h * d - asc[i - 1] * a + asc[i + m - 1]) % q
                if h in lookup:
                    print(h)
                    return i
                lookup.add(h)
            return -1

        q = 2 ** 63 - 1
        n = len(s)
        l = 0
        r = n
        pos = -1
        asc = [ord(x) - ord('a') for x in s]

        while l <= r:
            m = l + (r - l) // 2
            isFound = rabin_karp(m)
            if isFound != -1:
                l = m + 1
                pos = isFound

            else:
                r = m - 1
        return s[pos: pos + l - 1]





s = Solution2()
print(s.longestDupSubstring("banana"))
#"akyj"
print(s.longestDupSubstring("moplvidmaagmsiyyrkchbyhivlqwqsjcgtumqscmxrxrvwsnjjvygrelcbjgbpounhuyealllginkitfaiviraqcycjmskrozcdqylbuejrgfnquercvghppljmojfvylcxakyjxnampmakyjbqgwbyokaybcuklkaqzawageypfqhhasetugatdaxpvtevrigynxbqodiyioapgxqkndujeranxgebnpgsukybyowbxhgpkwjfdywfkpufcxzzqiuglkakibbkobonunnzwbjktykebfcbobxdflnyzngheatpcvnhdwkkhnlwnjdnrmjaevqopvinnzgacjkbhvsdsvuuwwhwesgtdzuctshytyfugdqswvxisyxcxoihfgzxnidnfadphwumtgdfmhjkaryjxvfquucltmuoosamjwqqzeleaiplwcbbxjxxvgsnonoivbnmiwbnijkzgoenohqncjqnckxbhpvreasdyvffrolobxzrmrbvwkpdbfvbwwyibydhndmpvqyfmqjwosclwxhgxmwjiksjvsnwupraojuatksjfqkvvfroqxsraskbdbgtppjrnzpfzabmcczlwynwomebvrihxugvjmtrkzdwuafozjcfqacenabmmxzcueyqwvbtslhjeiopgbrbvfbnpmvlnyexopoahgmwplwxnxqzhucdieyvbgtkfmdeocamzenecqlbhqmdfrvpsqyxvkkyfrbyolzvcpcbkdprttijkzcrgciidavsmrczbollxbkytqjwbiupvsorvkorfriajdtsowenhpmdtvamkoqacwwlkqfdzorjtepwlemunyrghwlvjgaxbzawmikfhtaniwviqiaeinbsqidetfsdbgsydkxgwoqyztaqmyeefaihmgrbxzyheoegawthcsyyrpyvnhysynoaikwtvmwathsomddhltxpeuxettpbeftmmyrqclnzwljlpxazrzzdosemwmthcvgwtxtinffopqxbufjwsvhqamxpydcnpekqhsovvqugqhbgweaiheeicmkdtxltkalexbeftuxvwnxmqqjeyourvbdfikqnzdipmmmiltjapovlhkpunxljeutwhenrxyfeufmzipqvergdkwptkilwzdxlydxbjoxjzxwcfmznfqgoaemrrxuwpfkftwejubxkgjlizljoynvidqwxnvhngqakmmehtvykbjwrrrjvwnrteeoxmtygiiygynedvfzwkvmffghuduspyyrnftyvsvjstfohwwyxhmlfmwguxxzgwdzwlnnltpjvnzswhmbzgdwzhvbgkiddhirgljbflgvyksxgnsvztcywpvutqryzdeerlildbzmtsgnebvsjetdnfgikrbsktbrdamfccvcptfaaklmcaqmglneebpdxkvcwwpndrjqnpqgbgihsfeotgggkdbvcdwfjanvafvxsvvhzyncwlmqqsmledzfnxxfyvcmhtjreykqlrfiqlsqzraqgtmocijejneeezqxbtomkwugapwesrinfiaxwxradnuvbyssqkznwwpsbgatlsxfhpcidfgzrc"))