# 1-indexed fenwick tree - be careful while updating and querying
def fenwick():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    bit = [0]*(len(a)+1)
    def query(n):
        # O(log N)
        ans = 0
        while n > 0:
            ans += bit[n]
            n -= (n&-n)
        return ans

    def update(i, val):
        # O(log N)
        while i < len(bit):
            bit[i] += val
            i += (i&-i)

    def build():
        # O(N)
        for i in range(len(a)):
            bit[i+1] += a[i]
            j = i+(i&-i)
            if j < len(bit):
                bit[j] += bit[i]

    build()
    print(query(6))
    update(2, 5) # Add 5 to the exisiting value
    print(query(6))

fenwick()