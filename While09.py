def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    sum_num=0
    while idx<len(s):
        sum_num+=int(s[idx])
        idx+=1
    
    return sum_num
print(main('12319156'))