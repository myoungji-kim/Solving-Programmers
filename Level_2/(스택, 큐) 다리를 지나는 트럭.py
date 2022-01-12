from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    wait = deque(truck_weights)
    bridge[-1] = wait.popleft()
    time = 1
    sum_bridge = bridge[-1]

    while wait or bridge.count(0) != bridge_length:
        temp = 0
        if wait:
            temp2 = sum_bridge + wait[0] - weight
            if bridge.count(0) != 0 and temp2 <= 0 or bridge[0] >= temp2:
                temp = wait.popleft()

        sum_bridge -= bridge.popleft()
        bridge.append(temp)
        sum_bridge += temp
        time += 1

    return time
