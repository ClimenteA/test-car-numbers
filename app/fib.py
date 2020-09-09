# program a function that returns n-th fibonacci number. 
# # f_(0) = 0 
# # f_(1) = 1 
# # f_(2) = f_(1) + f_(0) 
# # ... 
# # f_n = f_(n-1) + f_(n-2) 
# # f input values 0 1 2 3 4 5 6 7 
# # f output values 0 1 1 2 3 5 8 13 

cache = {} 
def recur_f_cached(n: int) -> int:
     
    if n == 0: 
        return 0 
    elif n == 1: 
        return 1 
    else: 
        if n in cache.keys(): 
            return cache[n] 
        else: 
            temp = recur_f_cached(n - 1) + recur_f_cached(n - 2) 
            cache[n] = temp 

    return temp 