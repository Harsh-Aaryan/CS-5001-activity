# Model output for task_238

## Model
- devstral-small-2:24b-cloud

## Original Code:

def number_of_substrings(str): 
	str_len = len(str); 
	return int(str_len * (str_len + 1) / 2); 

## Refactored Code:

```python
def number_of_substrings(str):
    str_len = len(str)
    return int(str_len * (str_len + 1) / 2)
```

- Preserved the exact function name `number_of_substrings` and its signature
- Maintained the original logic and return type (int)
- Kept the variable name `str_len` as in the original
- Ensured the calculation `str_len * (str_len + 1) / 2` remains unchanged
- Preserved the implicit return of the calculated value
- No additional functions were added or removed
- The function handles the input parameter `str` exactly as in the original
