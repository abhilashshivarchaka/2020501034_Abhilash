# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def fun_set_kth_digit(n, k, d):
    flag = False
    count = 0
    res = 1
    if(n < 0):
        n = -n
        flag = True

    while(n):
        r = n % 10
        if count == k:
            res += (d * (10 ** count))
        else:
            res = res + (r * (10 ** count))
        count += 1
        n = n // 10
        if(n==0):
            if count != k:
                res = res - (d * (10 ** (count-3)))
                if flag:
                    return(-res)
                else:
                    return res
            else:
                res=(res-1)+d*(10**count)
                if(flag):
                    return(-res)
                else:
                    return(res) 

    return(res)
