def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    sum_num=0
    while idx<len(s):
        if int(s[idx])%2!=0:
            sum_num+=int(s[idx])
        idx+=1
    
    return sum_num
print(main('11125'))