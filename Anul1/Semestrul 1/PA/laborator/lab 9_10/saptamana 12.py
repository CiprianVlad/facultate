#%%
M1 = [[8, 14, -6], 
     [12, 7, 4], 
     [-11, 3, 21]]

def del_maxElm(M1): 
    for i in range (0,len(M1)):
        maxim_line = max(M1[i])
        M1[i] = [x for x in M1[i] if x != maxim_line]
        
    return M1

del_maxElm(M1)
print(del_maxElm(M1))