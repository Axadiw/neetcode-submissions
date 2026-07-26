class Solution:
    def minWindow(self, s: str, t: str) -> str:
        histogram = {}
        min_substring = ""
        left = 0

        for letter in t:
            if not(letter in histogram):
                histogram[letter] = 0
            histogram[letter] += 1
        
        if len(s) < 1:
            return ""

        def add_to_histogram(letter_index):
            letter = s[letter_index]
            if not(letter in histogram):
                histogram[letter] = 0
            histogram[letter] += 1    
            # print(f"added {letter} to historam. it's now {histogram}")

        def remove_from_histogram(letter_index):
            letter = s[letter_index]
            histogram[letter] -= 1
            # print(f"removed {letter} from historam. it's now {histogram}")
        
        def is_histogram_empty():            
            # print(f"checking if {histogram} is empty")
            for value in histogram.values():
                if value > 0:
                    return False
            return True

        for right in range(len(s)):
            # print(f"new iteration: left: {left} right: {right}")
            if s[right] in histogram:
                # print(f"removing right {right} ({s[right]}) from histogram")
                remove_from_histogram(right)                
                
                if is_histogram_empty():
                    while left <= right:
                        if s[left] in histogram:
                            add_to_histogram(left)
                        left += 1

                        if not is_histogram_empty():
                            left -= 1
                            remove_from_histogram(left)
                            break

                    candidate = s[left:right+1]
                    # print(f'checking if {candidate} is a candidate')
                    if min_substring == '' or len(candidate) < len(min_substring):
                        # print(f'{candidate} is new min substring')
                        min_substring = candidate
            
            
        return min_substring