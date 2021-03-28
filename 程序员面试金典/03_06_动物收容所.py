from typing import List

class AnimalShelf:

    def __init__(self):
        self.qDog, self.qCat = [], []
        self.i, self.j = 0, 0
        self.count = 0

    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.qCat.append(animal + [self.count])
        else:
            self.qDog.append(animal + [self.count])
        self.count += 1

    def helper(self, cat) -> List[int]:
        if cat == 0:
            if self.j >= len(self.qCat):
                return [-1, -1, 20005]
            res = self.qCat[self.j]
        else:
            if self.i >= len(self.qDog):
                return [-1, -1, 20005]
            res = self.qDog[self.i]
        return res
    def dequeueAny(self) -> List[int]:
        res1, res2 = self.helper(0), self.helper(1)
        if res1[-1] < res2[-1]:
            if res1[1] != -1:
                self.j += 1
            return res1[:2]
        if res2[1] != -1:
            self.i += 1
        return res2[:2]

    def dequeueDog(self) -> List[int]:
        res = self.helper(1)
        if res[1] != -1:
            self.i += 1
        return res[:2]

    def dequeueCat(self) -> List[int]:
        res = self.helper(0)
        if res[1] != -1:
            self.j += 1
        return res[:2]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()