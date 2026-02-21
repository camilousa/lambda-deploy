import pandas as pd

def es_primo(n):
    for i in range(2, n):
      if n % i == 0:
        return False
        
    return True 


def handler(event, context):
    print("hello lambda from zappa")
    x = es_primo(5)
    return {}
    
    