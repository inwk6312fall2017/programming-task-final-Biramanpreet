book1=open('Book1.txt','r')
book2=open('Book2.txt','r')
book3=open('Book3.txt','r')
longest=0
for word in book1.read().split():
    if len(word) > longest:
        longest = len(word)
        longest_wordBook1 = longest
        abc=word
longest2=0
       
for word in book2.read().split():
    if len(word) > longest2:
        longest2 = len(word)
        longest_wordBook2 =longest2
        xyz=word
longest3=0
for word in book3.read().split():
    if len(word) > longest3:
        longest3 = len(word)
        longest_wordBook3 =longest3
        woa=word
if longest_wordBook1 > longest_wordBook2:
    if longest_wordBook1>longest_wordBook3:
       print("The longest word is  in Book1 ie. ",abc,"and its length is ",longest_wordBook1) 
    else:
       print("The longest word is in Book3 ie. " ,woa, "and its length is ",longest_wordBook3) 
elif longest_wordBook2 > longest_wordBook3:
    if longest_wordBook2>longest_wordBook1: 
       print("The longest word is  in Book2 ie. ",xyx,"and its length is ", longest_wordBook2) 
    else:
       print("The longest word is in Book1 ie. ",abc,"and its length is ",longest_wordBook1)    

else:
      print("The longest word is in Book3 ie. ",woa,"and its length is ",longest_wordBook3)    
   

