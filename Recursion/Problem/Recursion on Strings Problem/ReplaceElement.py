def ReplaceElement(s,a,x):
    n  = len(s)
    if n == 0:
        return s
    
    smallOutput = ReplaceElement(s[1:],a,x)
    
    if s[0] == a:
        return x + smallOutput
    
    else:
        return  s[0] + smallOutput
    
output = ReplaceElement("abbacaca",'a','c')

print(output)

