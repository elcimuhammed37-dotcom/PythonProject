#text= "hello python"
#result= text.center(20,'*')
#print(result)
#sayi=int("141",8)
#print(sayi)
#print(text.count("o",0,4))
#print("my name is {fName} .".format(fName="taha"))

# text="your life is "
# print(text , 5)
# result = 5
# print(x:=19)
# print(x)
names= ["ali","veli","kelie","bilie","kelie","muhsin"]
# print(names[-6:])
# print(numbers:=list(range(8)))
# deep=[ [ 5,6,7],[1,2,3,4],[8,2]]
# for item in deep:
#     for i in item:
#         print(f"{i} ",end=" ")
#     print()
# for index,item in enumerate(names,1):
#     print(f" {index}  - {item}",end=" ")
result=list(enumerate(names))
print(f"{result} {type(result)}")