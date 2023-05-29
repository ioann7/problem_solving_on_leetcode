# https://leetcode.com/problems/design-parking-system/

# Time complexity O(1). Space complexity O(1).
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parking[carType - 1] == 0:
            return False
        self.parking[carType - 1] -= 1
        return True
