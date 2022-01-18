def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    idx=0
    letter=0
    while idx<len(s):
        
        if  s[idx].isalpha() and s[idx]!='a' and s[idx]!='e' and s[idx]!='i' and s[idx]!='o' and s[idx]!='u' :
            
            letter+=1
        idx+=1
        
    
    return letter
print(main('123pi4appasappp'))
