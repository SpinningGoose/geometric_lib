# Library of basic calculations for geometric shapes

## Math formulas

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Functions

### rectangle.py

- area(a, b)

Description: caluculates area of a rectangle with set sides

Example:
```
from geometric_lib import rectangle

print(area(2, 3))

'6'
```

- perimeter(a, b)

Description: caluculates perimeter of a rectangle with set sides

Example:
```
from geometric_lib import rectangle

print(perimeter(2, 3))

'10'
```

### triangle.py

- area(a, h)

Description: caluculates area of a triangle with set side and height

Example:
```
from geometric_lib import triangle

print(area(2, 3))

'3'
```

- perimeter(a, b, c)

Description: caluculates perimeter of a triangle with set sides

Example:
```
from geometric_lib import triangle

print(perimeter(2, 3, 4))

'9'
```

### circle.py

- area(r)

Description: caluculates area of a circle with set radius

Example:
```
from geometric_lib import circle

print(area(1.0))

'3.141592653589793'
```

- perimeter(r)

Description: caluculates perimeter of a circle with set radius

Example:
```
from geometric_lib import circle

print(perimeter(1.0))

'6.283185307179586'
```

### square.py

- area(a)

Description: caluculates area of a square with set side

Example:
```
from geometric_lib import square

print(area(2))

'4'
```

- perimeter(a, b)

Description: caluculates perimeter of a square with set side

Example:
```
from geometric_lib import square

print(perimeter(2))

'8'
```

## History of commits

commit c718872d3856a4806ec14e918495c64638dfabea (HEAD -> lab2, origin/lab1, lab1)
Author: SpinningGoose <d7sh@yandex.ru>
Date:   Tue Dec 10 21:20:55 2024 +0300

    fix: rectangle perimeter formula

commit 3c88a5f781ad811f62660b1a7dc48eda431aef69
Author: SpinningGoose <d7sh@yandex.ru>
Date:   Tue Dec 10 21:18:46 2024 +0300

    feat: add rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
