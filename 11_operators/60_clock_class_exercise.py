

class Clock:
    def __init__(self, value):
        self._value = value
        
    def __str__(self):
        display_value = self._value % 12
        
        if display_value == 0:
            display_value = 12
            
        return f'{display_value} {'am' if (self._value % 24) < 12 else 'pm'}'
    
    
    # implementing add operator
    def __add__(self, other):
        return Clock(self._value + other._value)
    
    # implementing Unary operator / negative operators
    def __neg__(self):
        return Clock(self._value + 12)
    
    
        
        
        

def main():
    # c1 = Clock(7) # 7 am
    # c2 = Clock(19) # 7 pm
    # c3 = Clock(0) # 12 am
    # c4 = Clock(12) # 12 pm
    # c5 = Clock(25) # 1 am
    
    # print(c4 + c5)
    
    print(-Clock(9)) # change 9 am to 9 pm
    
    
    
main()