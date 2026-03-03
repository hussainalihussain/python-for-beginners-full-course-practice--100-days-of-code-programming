import random

# Encoding and Decoding (a secret message)
# if length of a string < 3 (reverse it)
# else
# move the first character to then end
# append and prepend 3-3 characters
'''
Example:
of hussain
-> fo ussainh
->-> fo ranussainhbae
'''

# at the end decode it too

message = input("Enter your message: ")

characters = [
  'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  '0','1','2','3','4','5','6','7','8','9'
]


def reverse(str):
  return ''.join(reversed(str))

def randomString(length):
  char = []

  for i in range(length):
    randomIndex = random.randint(0, len(characters) - 1)
    char.append(characters[randomIndex])

  return ''.join(char)



def encodeString(message):
  words = message.split(' ')
  newWords = []

  for i in range(len(words)):
    if len(words[i]) < 3:
      newWords.append(reverse(words[i]))

      continue
    
    firstCharacter = words[i][0]

    stringForPrepend = randomString(3)
    stringForAppend = randomString(3)

    newWords.append(stringForPrepend +  words[i][1:] + firstCharacter + stringForAppend)

  newString = ' '.join(newWords)

  return newString


def decodeString(string):
  words = string.split(' ')
  newWords = []

  for i in range(len(words)):
    currentWord = words[i]
    
    if len(currentWord) < 3:
      newWords.append(reverse(currentWord))
      continue

    newStr = currentWord[3:-3]
    newStr = newStr[-1] + newStr[:-1]

    newWords.append(newStr)
  
  return ' '.join(newWords)


encodedStr = encodeString(message)

print("Your encoded String:", encodedStr)
print()
print("And the is the decoded String:", decodeString(encodedStr))