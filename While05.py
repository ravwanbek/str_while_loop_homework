def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    letter=0
    while idx<len(s):
        if s[idx].islower():
            letter+=1
        idx+=1
    
    return letter
print(main('today is 15.01.20225T6jkhdalsk'))