from typing import Dict

def add(elem1: int, elem2: float) -> float:
    return elem1 + elem2

def add_dict(elem1: int, elem2: float) -> Dict:
    response = elem1 + elem2
    return {"soma": response}

val1 = add_dict(23, 1.2)
val2 = add(2, 12.35)
print(val1)
