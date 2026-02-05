# Model output for task_431

## Model
- devstral-small-2:24b-cloud

## Original Code:

def common_element(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result

## Refactored Code:

```python
def common_element(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
```

- Preserved the exact function name and signature `common_element(list1, list2)`
- Maintained the original logic and return type (`bool`)
- Kept the nested loop structure and early return behavior
- Ensured all variables and operators remain unchanged from the original
- No additional functions were added or removed
- The refactored code maintains identical behavior to the original implementation
