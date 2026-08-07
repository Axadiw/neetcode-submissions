class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ordered_letters = set()
        unordered_letters = set()
        orders = set()

        if len(words) == 0:
            return ""
        if len(words) == 1:
            return words[0]
        
        for i in range(1,len(words)):
            if len(words[i]) < len(words[i-1]) and words[i-1][:len(words[i])] == words[i]:
                print(f"incorrect order")
                return ""
            for l1_index in range(len(words[i-1])):                
                if len(words[i])-1 >= l1_index:
                    l1 = words[i-1][l1_index]
                    l2 = words[i][l1_index]    
                    if l1 == l2:
                        # print(f"comparing {l1} and {l2} from words {words[i-1]} and {words[i]}. The same - continuing")
                        if l1 not in ordered_letters:
                            unordered_letters.add(l1)
                        continue                
                    ordered_letters.add(l1)
                    if l1 in unordered_letters:
                        unordered_letters.remove(l1)
                    
                    orders.add((l1,l2))
                    if l2 not in ordered_letters:
                        unordered_letters.add(l2)
                    # print(f"comparing {l1} and {l2} from words {words[i-1]} and {words[i]}")
                    for l in words[i-1][l1_index+1:] + words[i][l1_index+1:]:
                        # print(f"checking {l} if it should not")
                        if l not in ordered_letters:
                            unordered_letters.add(l)
                    break
                
                if len(words[i]) > len(words[i-1]):
                    for l in words[i][len(words[i-1]):]:
                        if l not in ordered_letters:
                            unordered_letters.add(l)
                elif len(words[i-1]) > len(words[i]):
                    for l in words[i-1][len(words[i]):]:
                        if l not in ordered_letters:
                            unordered_letters.add(l)
                
        
        print(f"unordered_letters: {unordered_letters}")
        print(f"ordered_letters: {ordered_letters}")
        print(f"orders: {orders}")

        graph = {}
        for l1,l2 in orders:
            if l1 not in graph:
                graph[l1] = []
            graph[l1].append(l2)

        for l in unordered_letters:
            if l in graph:
                print(f"should not happen error")
                return ""
            graph[l] = []
        print(f"graph: {graph}")
        
        # detect cycles

        def dfs(letter, visited):
            if letter in visited:
                return True

            if len(graph[letter]) == 0:
                return False

            visited.add(letter)
            for l in graph[letter]:
                if dfs(l, visited.copy()):
                    return True
            return False
        
        for letter in list(ordered_letters) + list(unordered_letters):
            if dfs(letter, set()):
                print(f"cycle detected")
                return ""            
        
        
        visited = set()
        ret_val = []
        
        def traversal(letter):
            if letter in visited:
                return

            visited.add(letter)

            for l in graph[letter]:
                traversal(l)
            
            ret_val.append(letter)

        for letter in list(ordered_letters)+ list(unordered_letters):
            traversal(letter)
        
        return "".join(ret_val[::-1])
        
            