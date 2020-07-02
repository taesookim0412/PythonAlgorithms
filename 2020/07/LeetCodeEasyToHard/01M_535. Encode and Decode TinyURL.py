import collections
import string
from random import choice

#Runtime: 28 ms, faster than 91.94% of Python3 online submissions for Encode and Decode TinyURL.
#Memory Usage: 13.8 MB, less than 78.52% of Python3 online submissions for Encode and Decode TinyURL.

class Codec:
    def __init__(self):
        self.codes = collections.defaultdict(dict)
        self.urls = collections.defaultdict(dict)
        self.alphabet = string.ascii_letters + '0123456789'


    def encode(self, longUrl: str) -> str:
        while not self.codes[longUrl]:
            code = ''.join([choice(self.alphabet) for _ in range(6)])
            if not self.urls[code]:
                self.urls[code] = longUrl
                self.codes[longUrl] = code
        return self.codes[longUrl]


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[shortUrl]

# Your Codec object will be instantiated and called as such:
url = "ALKSD"
codec = Codec()
print(codec.decode(codec.encode(url)))