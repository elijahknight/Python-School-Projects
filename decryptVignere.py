Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> def letterToIndex(ch):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    idx = alphabet.find(ch)
    if idx < 0:
        print ("error: letter not in the alphabet", ch)
    return idx

>>> def indexToLetter(idx):
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

>>> def vignereIndex(keyLetter,plainTextLetter):
        keyIndex = letterToIndex(keyLetter)
        ptIndex = letterToIndex(plainTextLetter)
        newIdx = (ptIndex + keyIndex) % 26
        return indexToLetter(newIdx)

>>> def encryptVignere(key,plainText):
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

>>> def decryptVignere(key,cipherText):
	plainText = ""
	keyLen = len(key)
	charNum = 0
	for i in range(len(cipherText)):
		ch = cipherText[i]
		if ch == ' ';
		
SyntaxError: invalid syntax
>>>  def decryptVignere(key,cipherText):
	plainText = ""
	keyLen = len(key)
	charNum = 0
	for i in range(len(cipherText)):
		ch = cipherText[i]
		if ch == ' ':
			
SyntaxError: unexpected indent
>>> 
>>> def decryptVignere(key,cipherText):
	plainText = ""
	keyLen = len(key)
	charNum = 0
	for i in range(len(cipherText)):
		ch = cipherText[i]
		if ch == ' ':
			plainText = plainText + ch
		else:
			plainText = plainText + vignereIndex(key[i%keyLen],ch)
		return plainText

	
>>> def decryptVignere(key,cipherText):
	plainText = ""
	keyLen = len(key)
	charNum = 0
	for i in range(len(cipherText)):
		ch = cipherText[i]
		if ch == ' ':
			plainText = plainText + ch
		else:
			plainText = plainText + vignereIndex(key[i%keyLen],ch)
	return plainText

>>> encryptVignere("hellohello","hello world")
'oiwwc azczk'
>>> decryptVignere("hellohello", "oiwwc azczk")
'vmhhq eknnr'
>>> def decryptVignere(key,cipherText):
	plainText = ""
	keyLen = len(key)
	charNum = 0
	for i in range(len(cipherText)):
		ch = cipherText[i]
		if ch == ' ':
			plainText = plainText + ch
		else:
			plainText = plainText + vignereIndex(key[i%alphabet],ch)
	return plainText

>>> encryptVignere("hellohello","hello world")
'oiwwc azczk'
>>> decryptVignere("hellohello","oiwwc azczk")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    decryptVignere("hellohello","oiwwc azczk")
  File "<pyshell#29>", line 10, in decryptVignere
    plainText = plainText + vignereIndex(key[i%alphabet],ch)
NameError: name 'alphabet' is not defined
>>> def decryptVignere(key,cipherText):
	plainText = ""
	keyLen = len(key)
	charNum = 0
	for i in range(len(cipherText)):
		ch = cipherText[i]
		if ch == ' ':
			plainText = plainText + ch
		else:
			plainText = plainText + vignereIndex(key[i%keyLen],ch)
	return plainText

>>> def decVignereIndext(keyLetter, cipherTextLetter)
SyntaxError: invalid syntax
>>> def decVignereIndext(keyLetter, cipherTextLetter):
	keyIndex = letterToIndex(keyLetter)
	ctIndex = letterToIndex(cipherTextLetter)
	newIndex = (ctIndex - keyIndex) % 26
	return indexToLetter(newIndex)

>>> def decryptVignere(key,cipherText):
	plainText = ""
	keyLen = len(key)
	charNum = 0
	for i in range(len(cipherText)):
		ch = cipherText[i]
		if ch == ' ':
			plainText = plainText + ch
		else:
			plainText = plainText + decvignereIndext(key[i%keyLen],ch)
	return plainText

>>> encryptVignere("hellohello","hello world")
'oiwwc azczk'
>>> decryptVignere("hellohello","oiwwc azczk")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    decryptVignere("hellohello","oiwwc azczk")
  File "<pyshell#42>", line 10, in decryptVignere
    plainText = plainText + decvignereIndext(key[i%keyLen],ch)
NameError: name 'decvignereIndext' is not defined
>>> def decryptVignere(key,cipherText):
	plainText = ""
	keyLen = len(key)
	charNum = 0
	for i in range(len(cipherText)):
		ch = cipherText[i]
		if ch == ' ':
			plainText = plainText + ch
		else:
			plainText = plainText + decVignereIndext(key[i%keyLen],ch)
	return plainText

>>> encryptVignere("hellohello","hello world")
'oiwwc azczk'
>>> decryptVignere("hellohello","oiwwc azczk")
'hello world'
>>> keyGen()




