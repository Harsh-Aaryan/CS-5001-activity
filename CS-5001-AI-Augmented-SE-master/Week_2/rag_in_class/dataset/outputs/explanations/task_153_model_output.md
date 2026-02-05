# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a, b, c):
    vertex = (((-b / (2 * a)), (((4 * a * c) - (b * b)) / (4 * a))))
    return vertex
```

- Preserved the exact function name and signature `parabola_vertex(a, b, c)`
- Maintained the original calculation logic for the vertex coordinates
- Kept the return statement and tuple structure unchanged
- Ensured all operators and calculations match the original implementation
- No modifications were made to the algorithm or return types
- The function remains a direct translation of the original implementation
