# Model output for task_144

## Model
- devstral-small-2:24b-cloud

## Original Code:

def sum_Pairs(arr,n): 
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum

## Refactored Code:

```python
def sum_Pairs(arr, n):
    sum = 0
    for i in range(n - 1, -1, -1):
        sum += i * arr[i] - (n - 1 - i) * arr[i]
    return sum
```

- Preserved the exact function name `sum_Pairs` and its signature.
- Maintained the original logic and loop structure without modifications.
- Ensured the return type and value remain unchanged.
- Kept the variable names and operations as in the original implementation.
- Verified that no functions were removed or renamed.
- Confirmed that the algorithmic behavior is identical to the original.
