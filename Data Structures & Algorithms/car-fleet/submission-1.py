class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, v) for p, v in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, v in pair:  # Reverse Sorted Order
            stack.append((target - p) / v)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)