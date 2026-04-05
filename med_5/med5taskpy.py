"""
MEDIUM PROBLEM NO 5
you are programming a planetary rover equipped with a three-segment telescopic manipulator arm used for precision tasks. The arm consists of Inner, Middle, and Outer segments.
At any step, the arm configuration is represented as (Inner, Middle, Outer) and must satisfy:
Inner + Middle + Outer = Target
for the given target distance.
Each segment has a maximum extension limit:
0 ≤ Inner ≤ L1  
0 ≤ Middle ≤ L2  
0 ≤ Outer ≤ L3
To ensure stable operation of the manipulator, every configuration must also satisfy:
|Inner - Outer| ≤ D
If this condition is violated, the configuration is invalid.
The arm starts from the initial state (0, 0, 0) and retains its configuration after each target. Moving from one configuration to another incurs wear cost based on the movement of each segment:
Cost = |ΔInner| x W1 + |ΔMiddle| x W2 + |ΔOuter| x W3
where W1, W2, and W3 are the wear factors for the Inner, Middle, and Outer segments respectively.
Given a sequence of target distances, determine the minimum total wear cost required to reach all targets in order, using only valid configurations.

"""
#obtain all the required inputs from the user :
l1, l2, l3 = map(float, input("Enter limits L1, L2, L3: ").split())
w1, w2, w3 = map(float, input("Enter wear factors W1, W2, W3: ").split())
targets = list(map(float, input("Enter target values T1, T2, ..., Tn: ").split()))  
D = float(input("Enter maximum allowed difference D: "))

#the cost function deterimines the cost or effort of the arm in moving from one configuration to another and 
# we have to minimze this between moving.

def cost_fun(i1, i2, m1, m2, o1, o2):
    delta_inner = i2 - i1
    delta_outer = o2 - o1
    delta_middle = m2 - m1
    return abs(delta_inner)*w1 + abs(delta_middle)*w2 + abs(delta_outer)*w3
#intially posiiton: 0, 0, 0 
configs = [(0, 0, 0)]

#Greedy solution just proioritzes the current cost difference and doesnt care about the overall cost scenario
# this might be temporarily good but may return a bad solution overall
for target in targets:
    best_config = None
    prev_config = configs[-1]     #last configuration 
    min_cost = float('inf')       #initial large number
    for i1 in range(int(l1)+1):
        for m1 in range(int(l2)+1):
            for o1 in range(int(l3)+1):
                if(i1 + m1 + o1) != target: #check for target for target?
                    continue
                else:
                    cost = cost_fun(prev_config[0], i1, prev_config[1], m1, prev_config[2], o1) #other checking condition
                    if cost<min_cost:         #min cost seslection condition
                        if abs(i1 - o1)<=D:   #final condition
                            min_cost = cost 
                            best_config = (i1, m1, o1)
    print(f"Best config for target {target}: {best_config} with cost {min_cost}")
    configs.append(best_config)
print("Optimal configurations for targets:", configs[1:])


#new stratergy based on dp 
#This is not a greedy solution but rather looks onto the overall perspective when it comes to calculating the 
#target cost at the end
#this is more effecient and delivers the best solution directly
configs = [(0, 0, 0)]
dp = {(0, 0, 0): 0}  #initial dictionary
for target in targets:
    new_dp = {}
    for i1 in range(int(l1)+1):
        for o1 in range(int(l3)+1):
            m1=target - i1 -o1
            if not (0<=int(m1)<=l2): #check all the condititions given out 
                continue
            if abs(i1 - o1)>D:
                continue
            for (p1, pm ,po), prev_val in dp.items():  #now compare a valid configuration to each of the previous configurations from dp
                cost = prev_val + cost_fun(p1, i1, pm, m1, po, o1)
                key = (i1, m1, o1)   #The new configuration's minimum cost has to be stored in the new_dp
                if key not in new_dp or cost<new_dp[key]: 
                    new_dp[key]=cost 
    dp = new_dp        
    print(f"minimal total cost for when we reach the target {target} is", min(dp.values()))
    #The minimum of the costs presnt in new_dp is the minimum total cost overall to reach till that particular target


