#Даны две строки. Посчитайте сколько раз каждый символ первой строки 
# встречается во второй     «one» «onetwonine» - o – 2, n – 3, e – 2

phrase = 'one'
text = 'onetwonine'
count = 0
for j in range(len(phrase)):
    for i in range(len(text)):
        if phrase[j] == text[i]:
            count+=1
    print(f'{phrase[j]} - {count}', end =' , ')