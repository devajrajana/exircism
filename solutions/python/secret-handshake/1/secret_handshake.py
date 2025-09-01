def commands(binary_str):
    com=[]
    if binary_str[4]=='1':
        com.append('wink')
    if binary_str[3]=='1':
        com.append('double blink')
    if binary_str[2]=='1':
        com.append('close your eyes')
    if binary_str[1]=='1':
        com.append('jump')
    if binary_str[0]=='1':
        com.reverse()
    return com
        
    
    
        
    
