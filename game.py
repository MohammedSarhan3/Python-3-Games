#Game:  multiplication table
# start , end ---> multiplication table [start:end]

'''
start= int(input("Enter Start: ")) #cast
end= int(input("Enter Start: "))
for x in range(start,end+1):
    for y in range(1,11):
        print(f"{x} * {y} = {x*y}")
    print("----------------------") 
