f = open('filedata.txt','a')
f.write("sathunuru")
f.close()

f = open('filedata.txt')
print(f.read())
f.close()