class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ret_val = []
        letters = {}


        for l in s:
            if l not in letters:
                ret_val.append([1,[l]])
                letters[l] = len(ret_val) - 1
                print(f"{l} not found, adding to retval and letters dict. letters: {letters} ret_val: {ret_val}")
            else:                
                if letters[l] == len(ret_val) - 1:
                    # last word
                    ret_val[-1][0] += 1
                    print(f"{l} found and its in last word adding to it. letters: {letters} ret_val: {ret_val}")
                else:
                    print(f"{l} found earlier ret_val: {ret_val} letters: {letters}")
                    curr = ret_val[letters[l]]

                    
                    count = 1 + sum([x[0] for x in ret_val[letters[l]:]])
                    print(f"ret_val is {ret_val}, new letter is {l} merging everything thats after letters[l]={letters[l]}, that is {ret_val[letters[l]:]}")
                    new_letters = []
                    for array in [x[1] for x in ret_val[letters[l]:]]:
                        new_letters += array
                    print(f"new_letters: {new_letters}")
                    ret_val[letters[l]] = [count,new_letters]
                    ret_val = ret_val[:letters[l]+1]
                    
                    print(f"after recalculation ret_val would be {ret_val}")

                    for letter in new_letters:
                        print(f"setting word for letter {letter} to {letters[l]}")
                        letters[letter] = letters[l]
                    print(f"after recalculation letters would be {letters}")

                    # for key in letters.keys():
                    #     if letters[key] > letters[l]:
                    #         # print(f"setting word for letter {key} to {letters[l]}")
                    #         letters[key] = letters[l]
                    
                    
                        
        # print(f"final letters: {letters}")
        # print(f"final ret_val: {ret_val}")
        return [x[0] for x in ret_val]
            
        