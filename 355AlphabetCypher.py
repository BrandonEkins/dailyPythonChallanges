#https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/
import string
keyword = ""
message = ""
#create the cipher
cipher = dict()
tick = 0
for cap in string.ascii_uppercase:
    cipher[cap] = string.ascii_lowercase[tick:] + string.ascii_lowercase[:tick]
    tick += 1
#read in file
f = open("cipherfile.txt","r")
r = f.readline().split(" ")
keyword = r[0]
keywordIter = 0 
message = r[1]
encodedMessage = ""
for letter in message:
    encodedMessage += cipher[keyword[keywordIter].upper()][string.ascii_lowercase.find(letter)]
    keywordIter += 1
    if keywordIter == len(keyword):
        keywordIter = 0
print encodedMessage
