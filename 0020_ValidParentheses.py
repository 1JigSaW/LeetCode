def isValid(s: str) -> bool:
    actives_brackets=[]
    openings=["[","{","("]
    matchs={"[":"]","(":")","{":"}"}
    for bracket in s:
        if bracket in openings:
            actives_brackets.append(bracket)
            continue
        if not actives_brackets or bracket is not matchs[actives_brackets[-1]]:
            return False
        actives_brackets.pop()
            
    return len(actives_brackets)==0

print(isValid('([)]'))

