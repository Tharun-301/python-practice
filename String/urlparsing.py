url = input('Enter the url: ')
protocol = url[ : url.find(':')]                  # protocol = url[0:5]
dot1 = url.find('.')                              # Domain = url[12:18]
dot2 = url.find('.',dot1+1)   
domain = url[dot1+1:dot2]     
page = url[url.find('/',dot2) : ]                 # page = url[23:32]
print('protocol ',protocol)
print('Domain ',domain)
print('page ',page)


# https://www.kaggle.com//datasets
