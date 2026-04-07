# Mars Rover Telescopic Manipulator Arm - Optimization Problem

## Problem Statement

A planetary rover is equipped with a three-segment telescopic manipulator arm designed for precision tasks on extraterrestrial surfaces. The arm must be configured to reach specific target distances by extending its three segments: Inner, Middle, and Outer.

The core challenge is to find the minimum total wear cost required to transition the arm through a sequence of target distances while maintaining mechanical stability and respecting physical constraints.

## Input

- **L1, L2, L3**: Maximum extension limits for Inner, Middle, and Outer segments respectively
- **W1, W2, W3**: Wear factors (cost multipliers) for movement in each segment
- **D**: Maximum allowed difference constraint between Inner and Outer segments
- **Targets**: A sequence of target distances T1, T2, ..., Tn that the arm must reach in order

## Output

- **Minimum total wear cost**: The lowest cumulative cost to transition through all target configurations
- **Valid configurations**: For each target, a configuration tuple (Inner, Middle, Outer) that satisfies all constraints

## Constraints

For any valid configuration to reach a target:

1. **Sum constraint**: `Inner + Middle + Outer = Target`
2. **Range constraints**: 
   - `0 ≤ Inner ≤ L1`
   - `0 ≤ Middle ≤ L2`
   - `0 ≤ Outer ≤ L3`
3. **Stability constraint**: `|Inner - Outer| ≤ D`

## Cost Function

The wear cost of transitioning from configuration (i1, m1, o1) to (i2, m2, o2) is calculated as:

```
Cost = |Δinner| × W1 + |Δmiddle| × W2 + |Δouter| × W3
```

where Δ represents the change in each segment's extension.

---

## Approach

### 1. Greedy Solution (Not Optimal)

**Strategy**: At each target, select the configuration that minimizes the immediate cost from the current position.

**Algorithm**:
```
For each target:
  For all valid configurations (i, m, o) satisfying:
    - i + m + o = target
    - All range constraints
    - Stability constraint |i - o| ≤ D
  
  Find configuration with minimum cost from previous position
  Select this configuration regardless of future implications
```

**Why it fails**: The greedy approach makes locally optimal choices but lacks foresight. A configuration with slightly higher immediate cost might enable much cheaper transitions to subsequent targets. This myopic strategy frequently produces suboptimal overall solutions.

**Time Complexity**: O(n × L1 × L2 × L3) where n is number of targets

### 2. Dynamic Programming Solution (Optimal)

**Strategy**: Consider all valid configurations and track the minimum total cost to reach each configuration for every target.

**Algorithm**:
```
Initialize: dp = {(0,0,0): 0}  // starting position with zero cost

For each target:
  new_dp = {}
  
  For each possible configuration (i1, m1, o1):
    If configuration is invalid:
      Skip
    
    For each configuration (p1, pm, po) in current dp:
      Calculate total cost: prev_cost + transition_cost
      
      If this configuration exists in new_dp:
        new_dp[(i1, m1, o1)] = min(new_dp value, current total cost)
      Else:
        new_dp[(i1, m1, o1)] = current total cost
  
  dp = new_dp
```

**Key Insight**: We maintain ALL possible configurations with their minimum achieved costs, not just the best one. For each new target, we evaluate every valid configuration pair to find optimal transitions.

**Time Complexity**: O(n × K²) where K = total valid configurations per target

**Space Complexity**: O(K) where K = number of valid configurations

---

## Learning Takeaways

### 1. **Greedy ≠ Optimal**
Local optimization at each step doesn't guarantee global optimality. Problems with sequential dependencies require considering multiple future paths.

### 2. **State-Space Exploration**
Dynamic programming leverages dictionary/hash maps to store all previously computed states, enabling efficient lookup and update rather than recomputation.

### 3. **Trade-offs in Problem Solving**
- **Greedy**: Fast but potentially incorrect
- **DP**: Slower initially but guaranteed optimal results
- Always analyze whether the greedy assumption (current best = globally best) is valid

### 4. **Configuration Validity**
Multiple independent constraints (range, sum, stability) must be validated. Missing even one can lead to invalid solutions.

### 5. **Cost Function Importance**
The wear factors (W1, W2, W3) create asymmetric costs. Different problems may heavily favor certain segments, making the choice of segment for configuration much more complex.

### 6. **Dictionary-Based DP**
Using dictionaries/maps to track configurations and costs elegantly handles sparse solution spaces where not all combinations are valid or optimal.

---

## Algorithm Comparison

| Aspect | Greedy | Dynamic Programming |
|--------|--------|----------------------|
| **Optimality** | Not guaranteed | Guaranteed optimal |
| **Speed** | O(n·L1·L2·L3) | O(n·K²) |
| **Memory** | O(1) | O(K) |
| **Implementation** | Simple, intuitive | Requires state tracking |
| **Use Case** | Quick approximations | Need exact solution |

---

## Example Walkthrough

```
Inputs:
L1=5, L2=5, L3=5
W1=1, W2=1, W3=1
D=3
Targets: [5, 8]

Initial state: (0,0,0) with cost 0

Target 1 = 5:
  Valid configs: (0,0,5), (0,1,4), (0,2,3), ..., (5,0,0), etc.
  DP finds minimum cost from (0,0,0)
  
Target 2 = 8:
  From each config reached at target 1, find minimum cost paths
  DP considers all combinations, not just the "best" from target 1
```

---

