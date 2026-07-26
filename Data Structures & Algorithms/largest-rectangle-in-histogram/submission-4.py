from typing import NamedTuple

class Bar(NamedTuple):
    index: int
    height: int

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            if len(stack) == 0 or stack[-1].height <= h:
                stack.append(Bar(index=i,height=h))
                print(f"adding {stack[-1]}")
                continue
            else:
                print(f"barwith index {i} and height {h} is smaller than last one")
                last_item = stack[-1]                
                while len(stack) > 0 and stack[-1].height > h:
                    last_item = stack.pop()                
                    max_area = max(max_area, (i - last_item.index)*last_item.height)
                    print(f"Popped {last_item} from stack, max_area is {max_area} now")
                
                stack.append(Bar(index=last_item.index,height=h))

        print(f"finished with bars that could be extended to the end: {stack}")
        for bar in stack:
            max_area = max(max_area, (len(heights) - bar.index)*bar.height)

            


        return max_area