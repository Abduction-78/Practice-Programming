def even(n):
    if n % 2 == 0 :
        return True
    else:
        return False
    

f_num = 1
s_num = 2
sum = 0
while (f_num<4*10**6):
    new_num = f_num + s_num
    f_num = s_num
    s_num = new_num
    if even(f_num) == True:
        sum += f_num
        
print(sum)