def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    letter=0
    while idx<len(s):
        if s[idx].isalpha():
            letter+=1
        idx+=1
    
    return letter
print(main('today is 15.01.202256jkhdalsk'))