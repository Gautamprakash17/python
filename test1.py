a=[2,7,10,15,45,2,6,3,5,10,12,10,4,9]
for index in range(len(a)):
    print("indexes are:",a[index],"=",index)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        #print(a[j],end=' ')
        if a[i]+a[j]==9:
           print(a[i],a[j])
           print("its index is:-",i,j)

          
        