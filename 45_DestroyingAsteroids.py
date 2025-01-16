class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        s=[]
        asteroids.sort()
        for i in asteroids:
            s.append(i)
            while s and s[-1]<=mass:
                mass+=s.pop()
        return not s