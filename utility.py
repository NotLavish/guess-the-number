import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cwopy(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
    
def anyKey():
    os.system('pause')

def lengthChecker(data_type, target, limit):
    if data_type(target) != limit:
        if data_type(target) >= limit:
            lengthResult = "long"
            return lengthResult
        elif data_type(target) <= limit:
            lengthResult = "short"
            return lengthResult
    elif data_type(target) == limit:
        lengthResult = "pass"
        return lengthResult

def numCheck(target):
    try:
        int(target)
        numCheckResult = 'pass'
        return numCheckResult
    except ValueError:
        numCheckResult = 'fail'
        return numCheckResult