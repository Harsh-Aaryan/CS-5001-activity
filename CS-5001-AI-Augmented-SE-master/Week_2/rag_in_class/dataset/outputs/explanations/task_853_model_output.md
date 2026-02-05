# Model output for task_853

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def sum_of_odd_Factors(n): 
    res = 1
    while n % 2 == 0: 
        n = n // 2 
    for i in range(3,int(math.sqrt(n) + 1)): 
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            count+=1 
            n = n // i 
            curr_term *= i 
            curr_sum += curr_term    
        res *= curr_sum  
    if n >= 2: 
        res *= (1 + n) 
    return res 

## Refactored Code:

```python
import math

def sum_of_odd_Factors(n):
    res = 1
    while n % 2 == 0:
        n = n // 2
    for i in range(3, int(math.sqrt(n) + 1)):
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n >= 2:
        res *= (1 + n)
    return res
```

- Preserved the exact function name `sum_of_odd_Factors` and its signature
- Maintained all original logic, loops, and conditionals without modification
- Kept the same variable names and initialization
- Ensured the return statement and value type remain unchanged
- Did not add or remove any functions or code blocks
- Verified the implementation matches the original behavior exactly
