class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {}
        ret_val = []
        ret_val_set = set()
        for i in range(numCourses):
            courses[i] = set()
        
        for pre in prerequisites:
            courses[pre[0]].add(pre[1])
        # print(f"courses {courses}")
        for item in courses.items():
            # print(f"analyzing {item[0]}")
            def dfs(i,visited):
                # print(f"dfsing {i}")
                if len(courses[i]) == 0:
                    return [i]
                
                if i in visited:
                    return -1
                
                ret = [i]
                
                for preq in courses[i]:
                    visited.add(i)
                    prereqs = dfs(preq, visited)
                    visited.remove(i)
                    if prereqs == -1:
                        return -1
                    ret += prereqs
                return ret

            list_of_prereqs = dfs(item[0],set())
            # print(f"got {list_of_prereqs} as list_of_prereqs for {item[0]}")
            if list_of_prereqs == -1:
                return []

            for i in list_of_prereqs[::-1]:
                if not i in ret_val_set:
                    ret_val.append(i)
                    ret_val_set.add(i)
        
        return ret_val

                

        
                   