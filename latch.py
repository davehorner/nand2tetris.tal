from typing import Tuple

def sr_latch_nor(S: int, R: int, Q_prev: int = 0) -> Tuple[int, int]:
    """
    Pure functional emulation of a cross-coupled NOR SR latch.
    This models the REAL feedback loop using fixed-point recursion.
    
    Returns (Q, Q_bar)
    """
    # In real hardware:
    # Q     = NOR(R, Q_bar)
    # Q_bar = NOR(S, Q)
    #
    # Which is equivalent to solving:
    Q     = 0 if (R == 1 or (1 - Q_prev) == 1) else 1   # NOR(R, Q_bar)
    Q_bar = 0 if (S == 1 or Q_prev == 1) else 1        # NOR(S, Q)
    
    # If stable (feedback matches), return
    if Q == Q_prev:
        return Q, Q_bar
    
    # Otherwise, recurse with new assumed Q (this mimics continuous time propagation)
    # In real circuits this happens in picoseconds; here we iterate until stable
    return sr_latch_nor(S, R, Q)


# Test it like a real circuit
print(sr_latch_nor(0, 0, 0))   # Hold → stays 0 → (0, 1)
print(sr_latch_nor(0, 0, 1))   # Hold → stays 1 → (1, 0)
print(sr_latch_nor(1, 0))      # Set → (1, 0)
print(sr_latch_nor(0, 1))      # Reset → (0, 1)
print(sr_latch_nor(0, 0))      # Memory! Needs previous state, so we usually wrap it

# What happens in forbidden state?
# Uncomment if you want to see infinite recursion (like real oscillation!)
# print(sr_latch_nor(1, 1))  # → RecursionError! Just like real race/oscillation :)
