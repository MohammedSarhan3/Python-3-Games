#Game:  multiplication table
# start , end ---> multiplication table [start:end]

'''
start= int(input("Enter Start: ")) #cast
end= int(input("Enter Start: "))
for x in range(start,end+1):
    for y in range(1,11):
        print(f"{x} * {y} = {x*y}")
    print("----------------------") 


#Improve Game:  multiplication table As a function
#  start , end ---> multiplication table [start:end] 

def mul_table(start,end,mstart=1,mstop=10):
    for x in range(start,end+1):
        for y in range(mstart,mstop+1):
            print(f"{x} * {y} = {x*y}")
        print("----------------------")

        
mul_table(2,6,2,20)


#Game:  count words
# sentence : count words
sentence= input('Enter Sentence: ')
print(len(sentence.split()))


#improve Game:  count words as a function

# sentence : count words
def count_words(sentence):
    word_count=len(sentence.split())
    return word_count

sentence = "my name is mohammad"

print(count_words(sentence))
'''

