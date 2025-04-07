s1 = input()
s2 = input()
s1_len = len(s1)
s2_len = len(s2)

arr = [[0] * (s1_len + 1) for _ in range(s2_len + 1)]

#print(arr)

for i in range(s2_len):
    for j in range(s1_len):
        if s1[j] == s2[i]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

#for i in arr:
    #print(i)
print(arr[s2_len - 1][s1_len - 1])
'''
while True:
    if arr[x][y] == 0:
        break
    if arr[x][y - 1] == arr[x][y]:
        count += 1
        y -= 1
    elif arr[x - 1][y] == arr[x][y]:
        count += 1
        x -= 1
    else:
        x -= 1
        y -= 1
        if x < 0 or y < 0:
            count += 1
    if x < 0 or y < 0:
        break
    
print(count - 1)
'''
'''
Input: 
HKAHIKHEJW
MTHZEHCLSK
Expected: 3
Received: 2
    
Input: 
MWMHWCM
CMPOFVF
Expected: 2
Received: 1
    
Input: 
XEZE
KZED
Expected: 2
Received: 1
    
// 기타
Input: 
YZFXESWWYXMRKSKVKZWQXHEAIZTJXR
CEIKKZPCRITTROTRBSIMVUVHVJLKXF
Expected: 8
Received: 6

Input: 
IJXRGZNOIDXKITDXJOJUKACIPKMCSIGCKFDBSEFJDMPXOOQBCGIIEUOVCJLYWCKJIXSGVVFEKDBYELMTMKYSKGTUZHBKEEVIMNNR
BNUCZJTNQTGWUZMNDVOUBFFGNMIITIHQVRRFMYVIXOUPTLZDROLGFXVXOSVGUNILWJQVVXQMOQIULWDFPZZQOAVMBLUWSZOCSVDM
Expected: 30
Received: 18

ABCDEF
GBCDFE

XEZE
KZED

HKAHIKHEJW
MTHZEHCLSK

MWMHWCM
CMPOFVF

ACAYKP
CAPCAK
'''