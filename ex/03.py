import numpy as np
ary=np.arange(1,10)
print(ary,ary.shape)
ary.shape=(3,3)
print(ary,ary.shape)
print(ary,ary.dtype)
# ary.dtype='float32'
# print(ary,ary.dtype,ary.shape)
ary=ary.astype('float32')
print(ary,ary.size,len(ary))
print(ary[2,2])
ary=np.arange(1,28)
ary.shape=(3,3,3)
print(ary)
for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):
        for k in range(ary.shape[2]):
            print(ary[i,j,k])