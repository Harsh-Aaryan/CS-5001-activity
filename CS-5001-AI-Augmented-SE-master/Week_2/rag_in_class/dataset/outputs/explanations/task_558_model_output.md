# Model output for task_558

## Model
- devstral-small-2:24b-cloud

## Original Code:

def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))

## Refactored Code:

```python
def digit_distance_nums(n1, n2):
    return sum(map(int, str(abs(n1 - n2))))
```

- Preserved the exact function name and signature from the original implementation
- Maintained the original logic and return type (int)
- Ensured all operators and operations remain unchanged
- Kept the implicit return behavior
- Verified no functions were removed or renamed
- Preserved the exact algorithmic behavior as required by the tests
