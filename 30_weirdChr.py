
s = "try hello world"

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
ind_s = -1
ans = ""

for chr in s:
    ind_s = ind_s + 1

    if ind_s  % 2 == 0:
        ind_l = lower.index(chr)
        chr_upper = upper[ind_l]
        ans.   (chr_upper)
        
    elif ind_s % 2 == 1:
        ans.append(chr)
        
    else:
        ans.append(' ')
