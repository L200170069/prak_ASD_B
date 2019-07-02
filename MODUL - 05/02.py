pertama = [1,4,6,7,10,12]
kedua = [2,3,5,8,11]

def gabung(A,B):
    la = len(A)
    lb = len(B)
    c = list()
    i = 0
    j = 0
    while i < la and j < lb:
        if A[i] < B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    while i < la:
        c.append(A[i])
        i += 1
    while j > lb:
        c.append(B[j])
        j += 1
    return c

print("list pertama",pertama)
print("list kedua",kedua)
print("\nkedua list digabung menjadi ...\n")

print(gabung(pertama, kedua))
