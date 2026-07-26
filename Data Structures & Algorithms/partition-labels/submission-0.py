class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ret_val = []
        letters = {}

        for l in s:
            if l not in letters:
                ret_val.append(1)
                letters[l] = len(ret_val) - 1
                print(f"{l} not found, adding to retval and letters dict. letters: {letters} ret_val: {ret_val}")
            else:                
                if letters[l] == len(ret_val) - 1:
                    # last word
                    ret_val[-1] += 1
                    print(f"{l} found and its in last word adding to it. letters: {letters} ret_val: {ret_val}")
                else:
                    print(f"{l} found earlier")
                    ret_val[letters[l]] = 1 + sum(ret_val[letters[l]:])
                    ret_val = ret_val[:letters[l]+1]
                    print(f"fter recalculation ret_val would be {ret_val}")

                    for key in letters.keys():
                        if letters[key] > letters[l]:
                            print(f"setting word for letter {key} to {letters[l]}")
                            letters[key] = letters[l]
                    
                    
                        
        print(f"final letters: {letters}")
        print(f"final ret_val: {ret_val}")
        return ret_val
            
        