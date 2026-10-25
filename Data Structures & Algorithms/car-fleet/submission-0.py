class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 10-4 = 6/2 = 3
        # 10-1 = 9/2 = 4.5
        # 10-0 = 10/1 = 10
        # 19 - 7 = 3/1 = 3
        
        # sort the car array in descending order, where the car where the position is the closest is first
        # calculate how long it takes for i car to reach the destination. that time will be the minimum time

        # for i + 1 car, if it takes a shorter time for them to reach their destination, they will join the car fleet

        # if not, they are the only fleet

        if len(position) == 0:
            return 0
        car_fleets = 1

        pos_index = list(zip(position, speed))
        pos_index.sort(key=lambda x: -x[0])
        
        def calculate_eta(position, speed):
            return (target - position) / speed
        
        current_min = calculate_eta(pos_index[0][0], pos_index[0][1])
        
        for i in range(1, len(pos_index)):
            position, index = pos_index[i]
            eta = calculate_eta(position, index)
            if eta > current_min:
                car_fleets += 1
                current_min = eta
        return car_fleets
                
            