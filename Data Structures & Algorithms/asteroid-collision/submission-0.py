class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ret = []
        i = 0
        while i < len(asteroids):
            if i == len(asteroids) - 1:
                if abs(asteroids[i]) > abs(ret[-1]) or asteroids[i] * ret[-1] > 0:
                    ret.append(asteroids[i])
            elif asteroids[i] * asteroids[i + 1] > 0:
                ret.append(asteroids[i])
            elif abs(asteroids[i]) > abs(asteroids[i + 1]): 
                ret.append(asteroids[i])
                i += 1
            elif abs(asteroids[i]) == abs(asteroids[i + 1]):
                i += 1
            i += 1
        return ret


        