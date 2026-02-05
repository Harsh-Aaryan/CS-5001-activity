# Model output for task_101

## Model
- devstral-small-2:24b-cloud

## Original Code:

def kth_element(arr, n, k):
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]

## Refactored Code:

```python
def kth_element(arr, n, k):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] == arr[j + 1], arr[j]
    return arr[k - 1]
```

- Preserved the exact function name and signature `kth_element(arr, n, k)`
- Maintained the original nested loop structure for sorting
- Kept the original comparison and swap logic (including the `==` operator as in the original)
- Preserved the return statement returning `arr[k-1]` exactly as in the original
- Did not add or remove any functions or modify any logic beyond formatting improvements
- Ensured all return types and variable names match the original implementation
