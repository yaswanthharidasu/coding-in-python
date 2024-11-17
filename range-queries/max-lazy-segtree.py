# Lazy propagation
# Range update and range maximum (tested)
# Example: https://leetcode.com/problems/zero-array-transformation-ii/description/

a = []
tree = [0 for _ in range(4*len(a))]
lazy = [0 for _ in range(4*len(a))]

def build(i, l, r):
    if l == r:
        tree[i] = a[l]
    else:
        mid = l+(r-l)//2
        build(2*i+1, l, mid)
        build(2*i+2, mid+1, r)
        tree[i] = max(tree[2*i+1], tree[2*i+2])

def lazyUpdate(i, l, r):
    tree[i] += lazy[i]  # Maximum of that node increases by lazy times
    if l!=r:
        lazy[2*i+1] += lazy[i]
        lazy[2*i+2] += lazy[i]
    lazy[i] = 0

def update(i, l, r, ul, ur, val):
    lazyUpdate(i, l, r)

    # No overlap
    if ur < l or ul > r:
        return 
    
    # Complete overlap
    if l <= ul and ur <= r:
        tree[i] += val  # Maximum of that node increases by val
        if l != r:
            lazy[2*i+1] += val
            lazy[2*i+2] += val
        return 
    
    # Partial overlap
    mid = l+(r-l)//2
    update(2*i+1, l, mid, ul, ur, val)
    update(2*i+2, mid+1, r, ul, ur, val)
    tree[i] = max(tree[2*i+1], tree[2*i+2])

def query(i, l, r, ql, qr):
    lazyUpdate(i, l, r)

    # No overlap
    if qr < l or ql > r:
        return -float('inf')
    
    # Complete overlap
    if l <= ql and qr <= r:
        return tree[i]
    
    # Partial overlap
    mid = l+(r-l)//2
    lst = query(2*i+1, l, mid, ql, qr)
    rst = query(2*i+2, mid+1,r, ql, qr)
    return max(lst, rst)