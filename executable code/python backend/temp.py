# less=True
x=list(map(int,input().split()))
ans=[]
for i in range(len(x),0):
    less=True
    for j in range(i,len(x)):
        print(x[i],x[j],x[i]<x[j])
        if x[i]<x[j]:
            less=False
            break
    # print()    
    if less:
        ans.append(x[i])
print(ans)


    


