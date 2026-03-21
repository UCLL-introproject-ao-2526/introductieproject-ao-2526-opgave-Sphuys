import hashlib
import itertools
import string

target = "10ceee87f8b145ab495c3bca73b94455970159c6"
count = 0

for chars in itertools.product(string.ascii_uppercase, repeat=7):
    word = "".join(chars)
    h = hashlib.sha1(word.encode()).hexdigest()
    count += 1

    if count % 1000000 == 0:
        print("getest:", count, word)

    if h == target:
        print("gevonden:", word)
        break

## inderdaad duurt  dit veel te lang, dus heb ik het anders gedaan. 7 combinatie woorden geplakt in https://emn178.github.io/online-tools/sha1.html