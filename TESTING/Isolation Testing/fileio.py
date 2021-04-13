import os



#if os.path.exists('logs/readable.txt'):
#    print("exists")

with open('./TESTING/logs/filewritetest3.txt', 'w') as to_write:
    to_write.write("Joe is a penis")


# with open('logs/readable.txt', 'r') as to_send:
#     x = to_send.read()
#     print(x)
#     print("opened file")
# print(x)

#with open('./logs/readable.txt', 'a+') as log:
#
# with open('logs/readable.txt', 'r') as to_send:
# 	x = to_send.read()
# 	print(x)
# 	print("opened file")
# print(x)

f = open("./TESTING/logs/filewritetest3.txt", "r")
print(f.read())
