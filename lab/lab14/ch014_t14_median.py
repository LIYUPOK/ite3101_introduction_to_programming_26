from typing import List

def median(lst:List[int]) -> float:
    sorted_lst = sorted(lst)
    id len(sorted_lst) % 2 == 0:
    