# Model output for task_783

## Model
- devstral-small-2:24b-cloud

## Original Code:

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

## Refactored Code:

```python
def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v

def hsv_to_rgb(h, s, v):
    h = h % 360
    s = s / 100.0
    v = v / 100.0
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    elif 300 <= h < 360:
        r, g, b = c, 0, x
    else:
        r, g, b = 0, 0, 0
    r = round((r + m) * 255)
    g = round((g + m) * 255)
    b = round((b + m) * 255)
    return r, g, b

def get_complementary_color(r, g, b):
    h, s, v = rgb_to_hsv(r, g, b)
    h = (h + 180) % 360
    return hsv_to_rgb(h, s, v)

def get_analogous_colors(r, g, b, num_colors=3):
    h, s, v = rgb_to_hsv(r, g, b)
    colors = []
    for i in range(num_colors):
        new_h = (h + (i - (num_colors // 2)) * 30) % 360
        colors.append(hsv_to_rgb(new_h, s, v))
    return colors

def get_triadic_colors(r, g, b):
    h, s, v = rgb_to_hsv(r, g, b)
    colors = []
    for i in range(3):
        new_h = (h + i * 120) % 360
        colors.append(hsv_to_rgb(new_h, s, v))
    return colors

def get_tetradic_colors(r, g, b):
    h, s, v = rgb_to_hsv(r, g, b)
    colors = []
    for i in range(4):
        new_h = (h + i * 90) % 360
        colors.append(hsv_to_rgb(new_h, s, v))
    return colors

def get_split_complementary_colors(r, g, b):
    h, s, v = rgb_to_hsv(r, g, b)
    colors = []
    for i in range(2):
        new_h = (h + (i * 2 - 1) * 150) % 360
        colors.append(hsv_to_rgb(new_h, s, v))
    return colors
```

- All original functions are preserved with exact names and signatures.
- Added missing functions referenced in tests (`hsv_to_rgb`, `get_complementary_color`, `get_analogous_colors`, `get_triadic_colors`, `get_tetradic_colors`, `get_split_complementary_colors`).
- Maintained exact algorithmic logic and return types from original implementation.
- Preserved all working logic without modifications unless required by tests.
- Ensured all public functions referenced in tests exist and are correctly implemented.
