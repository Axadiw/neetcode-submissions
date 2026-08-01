class CountSquares:

    def __init__(self):
        self.points_x = {}
        self.points_y = {}
        self.counter = 0
        

    def add(self, point: List[int]) -> None:
        if point[0] not in self.points_x:
            self.points_x[point[0]] = []
        if point[1] not in self.points_y:
            self.points_y[point[1]] = []            

        self.points_x[point[0]].append((point[0],point[1],self.counter))
        self.points_y[point[1]].append((point[0],point[1],self.counter))
        self.counter+=1
        

    def count(self, point: List[int]) -> int:
        x,y = point[0], point[1]
        if x not in self.points_x or y not in self.points_y:
            return 0
        
        print(f">-START<")
        print(f"analyzing point {point}")
        print(f"points_x {self.points_x} points_y {self.points_y}")
        counter = 0

        for second_point in self.points_x[x]:
            print(f"analyzing second point {second_point} self.points_y[second_point[1]]: {self.points_y[second_point[1]]}")
            for third_point in self.points_y[second_point[1]]:
                
                if third_point == second_point:
                    # print(f"the same poit as second one, skipping")
                    continue
                print(f"analyzing third point {third_point}")
                for fourth_point in self.points_x[third_point[0]]:
                    print(f"analyzing fourth point {fourth_point}")
                    if (third_point[0],y) == (fourth_point[0],fourth_point[1]) and third_point != fourth_point:
                        if abs(third_point[0]-x) == abs(third_point[1]-y) and abs(third_point[1]-y)>0:
                            print(f"increasing counter first:{(x,y)} second:{second_point} third:{third_point} fourth:{fourth_point}")
                            counter +=1

        # print('<><><><>')
        # for second_point in self.points_y[y]:
        #     print(f"analyzing second point {second_point}")
        #     for third_point in self.points_x[second_point[0]]:
        #         if third_point == second_point:
        #             continue
        #         print(f"analyzing third point {second_point}")
        #         for fourth_point in self.points_x[third_point[0]]:
        #             print(f"analyzing fourth point {second_point}")
        #             if (x,third_point[1]) == fourth_point:
        #                 counter +=1
        print(f">-END<")
        return counter
        
