import random

def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText


def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]
    plainText = ""
    
    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]
        
    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]
    
    return plainText

def substitutionEncrypt (plainText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    
    return cipherText

def removeChar(string, idx):
    return string[:idx] + string[idx+1:]
    

def keyGen():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = ""
    for i in range(len(alphabet)):
        ch = random.randint(0,25-i)
        key = key + alphabet[ch]
        alphabet = removeChar(alphabet, ch)
        if len(alphabet) == 0:
            break
    return key

def removeDupes(myString):
    newStr = ""
    
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    
    return newStr

def removeMatches(myString, removeString):
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    
    return newStr

def genKeyFromPass(password):
   key = "abcdefghijklmnopqrstuvwxyz"
   password = removeDupes(password)
   lastChar = password[-1]
   lastIdx = key.find(lastChar)
   afterString = removeMatches(key[lastIdx+1:],password)
   beforeString = removeMatches(key[:lastIdx],password)
   key = password + afterString + beforeString
   
   return key

   
        
def letterToIndex(ch):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    idx = alphabet.find(ch)
    if idx < 0:
        print ("error: letter not in the alphabet", ch)
    return idx

def indexToLetter(idx):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    if idx > 26:
        print ('error: ', idx, ' is too large')
        letter = ''
    elif idx < 0:
        print ('error: ', idx, ' is less  than 0')
        letter = ''
    else:
        letter = alphabet[idx]
    return letter
    
print(encryptVignere("s","t"))

def vignereIndex(keyLetter,plainTextLetter):
        keyIndex = letterToIndex(keyLetter)
        ptIndex = letterToIndex(plainTextLetter)
        newIdx = (ptIndex + keyIndex) % 26
        return indexToLetter(newIdx)

def encryptVignere(key,plainText):
    cipherText = ""
    keyLen = len(key)
    charNum = 0
    for i in range(len(plainText)):
        ch = plainText[i]
        if ch == ' ':
            cipherText = cipherText + ch
        else:
            cipherText = cipherText + vignereIndex(key[i%keyLen],ch)
    return cipherText


