

def some_str(num_str):
    s=0
    for num in num_str:
        try:
            s+=int(num)
        except:
            pass
    return s



def persistence(number):
    str_num=number
    n=1
    p=1
    while len(str_num)!=1:
        for c in str_num:
            p*=int(c)
            str_num=str(p)
            p=1
            n+=1
    return n



def consecutive_sum(inters):
    s=[]
    num_count=dict()
    for val in inters:
        num_count[str(val)]=inters.count(val)
    for keys,val in num_count.items():
        s.append(int(keys)*int(val))
    return s

print(some_str(['2','42','ff']))
print(some_str(['1','2','3','gf','ff','4']))
print(persistence('999'))
print(persistence('67'))
print(consecutive_sum([0, 7, 7, 7, 5, 4, 9, 9, 0]))
print(consecutive_sum([4, 4, 5, 6, 8, 8, 8]))
print(consecutive_sum([-5, -5, 7, 7, 12, 0]))