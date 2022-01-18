
from string import whitespace


def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    idx=0
    alnum=0
    
    
    while idx<len(s):
        if not s[idx].isdigit() or s[idx].isalpha():
            alnum+=1
        idx+=1
    space=s.count(chr(32))
    
    

    return alnum-space
print(main('hlsnlds  1235ds8[]-*/++ ++++]`'))