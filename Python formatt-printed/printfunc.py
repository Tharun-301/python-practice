#separator
print('hello', 21, 9)#it takes automatically separate the values
print('hello',21,9,sep=' ')
print('hello',21,9,sep='_')
print('hello',21,9,sep='*')
print('Hello ',end='\t')
print('world')
##not supported file=sys.stdout
print('Hello world',sep='@',end='\n', flush=True)#flush is default false, not required mostly, but sometimes.



