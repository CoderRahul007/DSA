# You are given a 0-indexed integer array buses of length n, where buses[i] represents the departure time of the ith bus. You are also given a 0-indexed integer array passengers of length m, where passengers[j] represents the arrival time of the jth passenger. All bus departure times are unique. All passenger arrival times are unique.

# You are given an integer capacity, which represents the maximum number of passengers that can get on each bus.

# When a passenger arrives, they will wait in line for the next available bus. You can get on a bus that departs at x minutes if you arrive at y minutes where y <= x, and the bus is not full. Passengers with the earliest arrival times get on the bus first.

# More formally when a bus arrives, either:

# If capacity or fewer passengers are waiting for a bus, they will all get on the bus, or
# The capacity passengers with the earliest arrival times will get on the bus.
# Return the latest time you may arrive at the bus station to catch a bus. You cannot arrive at the same time as another passenger.

# Note: The arrays buses and passengers are not necessarily sorted.


# Example 1:

# Input: buses = [10,20], passengers = [2,17,18,19], capacity = 2
# Output: 16
# Explanation: Suppose you arrive at time 16.
# At time 10, the first bus departs with the 0th passenger.
# At time 20, the second bus departs with you and the 1st passenger.
# Note that you may not arrive at the same time as another passenger, which is why you must arrive before the 1st passenger to catch the bus.


# Rationale
# We could imagine the time given in the passengers Array to be a seat.
#  A passenger may take a seat only if it is not taken already.
#  The problem then boils down to finding the last possible seat for our candidate.
# This analogy makes it easier to visualize the problem
# Since we would like our candidate to take the last seat, we could find the last
# possible seat number that they could take
# Fit as many people as possible in every bus until you max out. We could sort the Arrays to make it easier
# The maximum seat would either be the last seat in the last bus if it is maxed out or the bus capacity (buses[-1])
# Iterate backwards from the last possible seat, if it is available, allocate it
# Complexities
# Time: O(blogb + plogp)
# Space: O(p)

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        passenger = 0
        for departure_time in buses:
            maxed = False
            cap = capacity

            # fill every passenger according to capacity
            while passenger < len(passengers) and passengers[passenger] <= departure_time and cap != 0:
                passenger += 1
                cap -= 1
            if cap == 0:
                maxed = True  # when everyone filled the maxed out

        if maxed:
            max_seat = passengers[passenger-1]  # last seat
        else:
            max_seat = buses[-1]

        booked = set(passengers)
        for seat in range(max_seat, 0, -1):  # till 1
            if seat not in booked:
                return seat


# Using minheap
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:

        minHeap = []
        # Complexity of building heap is O(P)
        for p in passengers:
            heapq.heappush(minHeap, p)
        # Complexity of sorting buses is O(BlogB)
        buses.sort()
        ans = 0
        arrived_arr = set()
        # Complexity of below loop: O(B + PlogP)
        for bus_departure in buses:
            temp_cap = 0
            while minHeap and minHeap[0] <= bus_departure and temp_cap < capacity:
                p = heapq.heappop(minHeap)
                arrived_arr.add(p)
                temp_cap += 1
                if p-1 not in arrived_arr:
                    ans = p-1
            if temp_cap < capacity and bus_departure not in arrived_arr:
                ans = bus_departure # bus still have capicity for us, then we just arrive on time. at buses departure time
        return ans

    # Total complexity: O(P)+O(BlogB)+O(B + PlogP)
    # Overall complexity: O(BlogB + PlogP)
