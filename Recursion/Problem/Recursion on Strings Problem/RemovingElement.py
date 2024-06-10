def RemovingElement(s,x):
    n = len(s)

    if n == 0:
        return s
    
    smallOutput = RemovingElement(s[1:], x)

    if s[0] == x:
        return RemovingElement(s[1:], x)
    
    else:
        return s[0] + RemovingElement(s[1:],x)
    

output = RemovingElement("abcccabc","c")
print(output)