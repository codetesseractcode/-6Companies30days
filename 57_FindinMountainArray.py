class Solution:
    def findInMountainArray(self, t: int, arr: 'MountainArray') -> int:
        peak = self.findpeak(arr)
        firstTry = self.oabs(arr, t, 0, peak)
        if firstTry != -1:
            return firstTry
        return self.oabs(arr, t, peak + 1, arr.length() - 1)

    def findpeak(self, arr):
        s = 0
        e = arr.length() - 1

        while s < e:
            m = s + (e - s) // 2
            if arr.get(m) > arr.get(m + 1):
                e = m
            else:
                s = m + 1

        return s

    def oabs(self, arr, t, s, e):
        isAsc = arr.get(s) < arr.get(e)

        while s <= e:
            m = s + (e - s) // 2

            if arr.get(m) == t:
                return m
            if isAsc:
                if t > arr.get(m):
                    s = m + 1
                else:
                    e = m - 1
            else:
                if t < arr.get(m):
                    s = m + 1
                else:
                    e = m - 1

        return -1