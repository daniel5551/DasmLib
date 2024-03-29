digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
lower = ('a','b','c','d','e','f','g','h',
        'i', 'j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z')
upper = ('A','B','C','D','E','F','G','H',
        'I','J','K','L','M','N','O','P','Q',
        'R','S','T','U','V','W','X','Y','Z')
        
letters = lower+upper

def ord(char: str):
    if char in letters:
        return letters.index(char)
    else:
        return -1

def char(code: int) -> str:
    if code <= len(letters) or code >= 0:
        return letters[code]
    else:
        return -1

def isUpper(char: str) -> bool:
    if ord(char) >= ord('A') or ord(char) <= ord('Z'):
        return True
    else:
        return False

def isLower(char: str) -> bool:
    if ord(char) >= ord('a') or ord(char) <= ord('z'):
        return True
    else:
        return False
