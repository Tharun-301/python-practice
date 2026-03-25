# #find
# s1 = 'Hello how are you'
# print(s1.find('how'))
# print(s1.rfind('o'))
# print(s1.index('h'))
# #just
# s2 = 'Hello'
# print(s2.ljust(7,'*'))
# print(s2.rjust(7,'*'))
# print(s2.center(7,'*'))
# print(s2.zfill(7))
# #Strip
# s3 = '  World'
# s4 = 'world@@@@##'
# s5 = '##Hello###'
# s6 = '##!@ Tharun !*% '
# print(s3.lstrip(''))
# print(s4.rstrip('@#'))
# print(s5.strip('#'))
# print(s6.strip('#!@ !*%'))
#replace
# s  = 'tharun@yahoo.com'
# print(s.replace('yahoo','gmail'))
#join we can join words, we can use split
# s1 = '/'
# s3 = 'xyz'
# s2  = 'abcd'
# print(s1.join(s2))
# print(s3.join(s2))
s1 = 'john_smith_jason_Tharun_sathunuru'
print(s1.split('_',2))#next
print(s1.rsplit('_',3))
s3 = 'All\nthis\nmethods\nwill\nreturn\nnew\nstring'
print(s3.splitlines())
s = 'python is very easy'
print(s.startswith('is',7))
print(s.endswith('easy',15))
print(s.removeprefix('py'))
print(s.removesuffix('easy'))
print(s.partition('is'))
print(s.rpartition('s'))
print(True+True)