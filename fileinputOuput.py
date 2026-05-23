# f  = open("demo.txt", "rt")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f  = open("demo.txt", "rt")
# data = f.read(10)
# print(data)
# print(type(data))
# f.close()

# f  = open("demo.txt", "rt")
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# f.close()

# #writing inside  a file
# f  = open("demo.txt", "w")
# f.write("i want to do all the tasks 999")
# f.close()
# f  = open("demo.txt", "a")
# f.write("\nthen i will watch the series")
# f.close()

# #this creates a new file the respective folder
# f = open("sample.txt", "w")
# f.close()
# #or this way also..
# f = open("sample.txt", "a")
# f.close()

# #override
# f = open("demo.txt", "r+")
# f.write("Abc")
# print(f.read())
# f.close()

# f = open("demo.txt", "w+")
# f.write("abcs")
# print(f.read())
# f.close()

# f = open("demo.txt", "a+")
# f.write("abcs")
# print(f.read())
# f.close()

# #"with" syntax -> automatically closes the file, hence no need of close()
# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f: 
#     f.write("new data!!")

# import os
# os.remove("demo.txt")

# #practice qns
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java")

# with open("practice.txt", "r") as f:
#     data  = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data )

# with open("practice.txt", "w") as f:
#     f.write(new_data)
   
# word = "learning" 
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not found")
        
# def check_for_word():
#     word = "learning" 
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not found")
# check_for_word()

# def check_for_line():
#     word = "nice"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# print(check_for_line())
            
with open("practice.txt", "r") as f:
    data =  f.read()
    print(data)
    
    num =""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num =""
        else:
            num += data[i]

count = 0       
with open("practice.txt", "r") as f:
    data =  f.read()
  
    
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)
            
