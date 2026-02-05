# Model output for task_392

## Model
- devstral-small-2:24b-cloud

## Original Code:

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

## Refactored Code:

```python
def get_max_sum(n):
    res = list()
    res.append(0)
    res.append(1)
    i = 2
    while i < n + 1:
        res.append(max(i, (res[int(i / 2)]
                          + res[int(i / 3)]
                          + res[int(i / 4)]
                          + res[int(i / 5)])))
        i = i + 1
    return res[n]
```

- Preserved the exact function name `get_max_sum` and its signature
- Maintained the original algorithmic logic including the while loop and max calculation
- Kept the original return type and value format
- Ensured all variables and operations remain unchanged from the original implementation
- Preserved the list initialization and append operations exactly as in the original
- Maintained the integer division operations as specified in the original code
- Kept the implicit return behavior of the original function
- Ensured the function handles the input parameter `n` exactly as in the original implementation
