class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        shand = sorted(hand)
        # print(f"shand: {shand}")
        chand = []

        i = 0
        while i < len(shand) and len(shand) + len(chand) >= groupSize:
            # print(f"analyzing i={i}")
            if len(chand) == 0:
                chand.append(shand.pop(i))
                # print(f"added card to hand, hand {chand} left: {shand}")
                if len(chand) == groupSize:
                    chand = []
                    i = 0     
                    # print(f"immediately checking that hand is full =  {chand} resetting hand and setting i = 0")
                continue

            if len(chand) == groupSize:
                # print(f"hand full =  {chand} resetting hand and setting i = 0")
                chand = []
                i = 0     
                continue           

            diff = chand[-1] - shand[i]
            if diff == -1:                
                chand.append(shand.pop(i))                
                # print(f"adding incremental card to hand. hand {chand} left: {shand}")
                if len(chand) == groupSize:
                    chand = []
                    i = 0     
                    # print(f"immediately checking that hand is full =  {chand} resetting hand and setting i = 0")
            elif diff == 0:
                # print(f"skipping the same card")
                i += 1
            else:
                # print(f"too large card, setting it's failure")
                return False

            
        
        # print(f"state at the end: hand {chand} shand: {shand}")
        return len(shand) == 0 and len(chand) == 0
        