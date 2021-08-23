num_str=['1','2','kdjf','3','ff','4']
def some_str():
    s=0
    for num in num_str:
        try:
            s+=int(num)
        except:
            pass
    print(s)
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
inters=[0, 7, 7, 7, 5, 4, 9, 9, 0]
def consecutive_sum():
    s=[]
    num_count=dict()
    for val in inters:
        num_count[str(val)]=inters.count(val)
    for keys,val in num_count.items():
        s.append(int(keys)*int(val))
    print(s)

consecutive_sum()

