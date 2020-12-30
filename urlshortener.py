import pyshorteners
url=input("Enter the URL: ")
shortener=pyshorteners.Shortener()
a=shortener.tinyurl.short(url)
print(a)