def stuff(signal):
    one_cn = 0  
    index_cn = 0   
    one = [] 
    s = list(signal)
    for i in s:
        index_cn += 1
        if i == '0':
            one_cn = 0
        else:
            one_cn += 1
        if one_cn == 5:
            one.append(index_cn)
            one_cn = 0
    k = 0  
    for i in one:   
        
        s.insert(i + k, '0')
        k += 1
    return s

def destuff(signal):
    one_cn = 0
    index_cn = 0
    one = []
    sig = list(signal)
    for i in sig:
        index_cn += 1
        if i == '0':
            one_cn = 0
        else:
            one_cn += 1
        if one_cn == 5:
            one.append(index_cn)
            one_cn = 0
    k = 0
    for i in one:
        sig.pop(i+k)
        k -= 1
    return sig
signal = input("Enter the signal: ")
print("Original Signal : ", signal)
stf = stuff(signal)
print("Stuffed Signal : ", end="")
print("".join([x for x in stf]))
dstf = destuff(stf)
print("Destuff Signal : ", end="")
print("".join([x for x in dstf]))

