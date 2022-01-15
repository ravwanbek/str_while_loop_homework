def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    b=[]
    while idx<10:
        a=s.count(str(idx))
        b.append(a)
       
        idx+=1
    
    
    
        
    return sum(b)
print(main('today is 15.01.202256'))