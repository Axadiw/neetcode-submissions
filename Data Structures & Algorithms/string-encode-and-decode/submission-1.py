class Solution:

    def encode(self, strs: List[str]) -> str:
        returnString = ""
        for singleStr in strs:
            for letter in singleStr:
                returnString += letter
            returnString += chr(110000)
        
        print(f"Will return {returnString}")
        return returnString

    def decode(self, s: str) -> List[str]:
        returnTable = []

        currentString = ""
        for possibleLetter in s:
            if ord(possibleLetter) == 110000:
                # if len(currentString) > 0:
                returnTable.append(currentString)
                currentString = ""
            else:
                currentString += possibleLetter
        
        return returnTable
