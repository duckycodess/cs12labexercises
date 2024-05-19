def k_smooth(n: int, k: int) -> bool:
    return True if n == 1 else (k_smooth(n//k, k) if n % k == 0 else (k_smooth(n, k-1) if k % 2 == 0 or k == 3 else k_smooth(n, k-2))) if k > 1 and n > 1 else False

def smooth_with_k(n: int, k: int) -> int:
    return k+1 if not k_smooth(n, k) else smooth_with_k(n, k-1)

def smoothness_param(n: int) -> int:
    return smooth_with_k(n, int((n)**(1/2)+1))