vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
question = input()
i = len(question) - 1
while i >= 0 and (question[i] == ' ' or question[i] == '?'):
    i -= 1
while i >= 0 and not question[i].isalpha():
    i -= 1

if question[i].upper() in vowels:
    print("YES")
else:
    print("NO")
