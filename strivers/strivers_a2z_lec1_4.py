from typing import List
from math import pi

def areaSwitchCase(ch: int, a: List[float]) -> float:
    res = 0
    match ch:
        case 1:
            res = pi * a[0] * a[0]
        case 2:
            res = a[0] * a[1]
    return '{:.5f}'.format(res)

print(areaSwitchCase(1, [2])) # 12.56637
