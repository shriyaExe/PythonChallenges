import sys
import random

class WaveletTree:
    def __init__(self, from_, to, x, y):
        self.lo = x
        self.hi = y
        if self.lo == self.hi or from_ >= to:
            return
        self.b = [0]
        mid = (self.lo + self.hi) // 2
        f = lambda x: x <= mid
        left_array = list(filter(f, from_))
        right_array = list(filter(lambda x: not f(x), from_))
        self.b += [len(left_array)] * len(from_)
        for i in range(1, len(self.b)):
            self.b[i] += self.b[i-1]
        pivot = len(left_array)
        self.l = WaveletTree(from_[:pivot], from_[:pivot], self.lo, mid)
        self.r = WaveletTree(from_[pivot:], from_[pivot:], mid + 1, self.hi)
    
    def kth(self, l, r, k):
        if l > r:
            return 0
        if self.lo == self.hi:
            return self.lo
        in_left = self.b[r] - self.b[l - 1]
        lb = self.b[l - 1]
        rb = self.b[r]
        if k <= in_left:
            return self.l.kth(lb + 1, rb, k)
        return self.r.kth(l - lb, r - rb, k - in_left)
    
    def LTE(self, l, r, k):
        if l > r or k < self.lo:
            return 0
        if self.hi <= k:
            return r - l + 1
        lb = self.b[l - 1]
        rb = self.b[r]
        return self.l.LTE(lb + 1, rb, k) + self.r.LTE(l - lb, r - rb, k)
    
    def count(self, l, r, k):
        if l > r or k < self.lo or k > self.hi:
            return 0
        if self.lo == self.hi:
            return r - l + 1
        lb = self.b[l - 1]
        rb = self.b[r]
        mid = (self.lo + self.hi) // 2
        if k <= mid:
            return self.l.count(lb + 1, rb, k)
        return self.r.count(l - lb, r - rb, k)

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(data[idx])
        idx += 1
    T = WaveletTree(a[1:], a[n+1:], 1, int(1e6))
    q = int(data[idx])
    idx += 1
    result = []
    while q > 0:
        q -= 1
        x = int(data[idx])
        idx += 1
        l = int(data[idx])
        idx += 1
        r = int(data[idx])
        idx += 1
        k = int(data[idx])
        idx += 1
        if x == 0:
            result.append(f"Kth smallest: {T.kth(l, r, k)}")
        elif x == 1:
            result.append(f"LTE: {T.LTE(l, r, k)}")
        elif x == 2:
            result.append(f"Occurrence of K: {T.count(l, r, k)}")
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()
