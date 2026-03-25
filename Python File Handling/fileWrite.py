# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()



# file = open('context.txt','w')
 
# lst = ["one\n","two\n","three\n","four\n","five"]

# # file.truncate(lst)
# file.writelines(lst)
# file.close