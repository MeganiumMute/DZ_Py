word=input('Введите слово\n')
if len(word)%2==0:
    print(word[len(word)//2-1:len(word)//2+1])
elif len(word)%2>0:
    print(word[len(word)//2])
    print(len(word)//2)