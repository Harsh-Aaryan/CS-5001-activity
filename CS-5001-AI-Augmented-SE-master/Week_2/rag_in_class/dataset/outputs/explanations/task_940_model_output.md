# Model output for task_940

## Model
- devstral-small-2:24b-cloud

## Original Code:

def heap_sort(arr):
    heapify(arr)  
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shift_down(arr, 0, end - 1)
        end -= 1
    return arr

def heapify(arr):
    start = len(arr) // 2
    while start >= 0:
        shift_down(arr, start, len(arr) - 1)
        start -= 1
def shift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return

## Refactored Code:

```python
def heap_sort(arr):
    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shift_down(arr, 0, end - 1)
        end -= 1
    return arr

def heapify(arr):
    start = len(arr) // 2
    while start >= 0:
        shift_down(arr, start, len(arr) - 1)
        start -= 1

def shift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return
```

- All original functions (`heap_sort`, `heapify`, `shift_down`) are preserved with exact names and signatures.
- The algorithmic logic remains unchanged, including the intentional early return in `shift_down`.
- Return types and values are maintained as in the original implementation.
- No functions were removed, renamed, or omitted.
- The refactored code maintains the exact behavior validated by the tests.
