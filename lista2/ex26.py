dic1 ={
    "um":1,
    "dois":2,
    "tres":3,
    "quatro":4
}
dic2 ={
    "um":1,
    "cinco":5,
    "tres":3,
    "seis":6
}

def merging(dic1, dic2):
    dic3 = dic1.copy()
    
    for x, y in dic2.items():
        if x in dic3:
            dic3[x] += y
        else:
            dic3[x] = y
            
    return dic3

dic3 = merging(dic1, dic2)
print(dic3)