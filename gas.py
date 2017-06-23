# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
#
# Return the minimum starting gas station’s index if you can travel around the circuit once, otherwise return -1.
#
# You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2..
# Completing the circuit means starting at i and ending up at i again.
#
# Example :
#
# Input :
#       Gas :   [1, 2]
#       Cost :  [2, 1]
#
# Output : 1
#
# If you start from index 0, you can fill in gas[0] = 1 amount of gas. Now your tank has 1 unit of gas.
# But you need cost[0] = 2 gas to travel to station 1.
#
# If you start from index 1, you can fill in gas[1] = 2 amount of gas. Now your tank has 2 units of gas.
# You need cost[1] = 1 gas to get to station 0. So, you travel to station 0 and still have 1 unit of gas left over.
# You fill in gas[0] = 1 unit of additional gas, making your current gas = 2.
# It costs you cost[0] = 2 to get to station 1, which you do and complete the circuit.
#

class Solution:
    # @param gas : tuple of integers
    # @param cost : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        cumm_gas, cum_cost = 0,0
        tank,start = 0,0
        for i in range(len(gas)):
            cumm_gas += gas[i]
            cum_cost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i+1
        if cumm_gas < cum_cost: return -1
        return start

# My Solution:
class Solution:
    # @param gas : tuple of integers
    # @param cost : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum([(gas[i] - cost[i]) for i in xrange(len(gas))]) < 0:
            return -1

        for j in xrange(len(gas)):
            gas_left = gas[j] - cost[j]
            next_station = (j + 1) % len(gas)
            while gas_left >= 0:
                gas_left = gas_left + (gas[next_station] - cost[next_station])
                next_station = (next_station + 1) % len(gas)
                if next_station == j:
                    return j
        return -1
