def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    even_num=0
    while idx<len(s):
        if int(s[idx]) % 2==0:
            even_num+=1
        idx+=1
    
    return even_num
print(main('82341095161'))
