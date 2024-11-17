# Lazy propagation
# Range update and range sum (not tested)

a = []
tree = [0 for _ in range(4*len(a))]
lazy = [0 for _ in range(4*len(a))]

def build(i, l, r):
    # Leaf noe
    if l == r:
        tree[i] = a[l]
    else:
        mid = l+(r-l)//2
        build(2*i+1, l, mid)
        build(2*i+2, mid+1, r)
        tree[i] = tree[2*i+1] + tree[2*i+2]

def lazyUpdate(i, l, r):
    tree[i] += (r-l+1)*lazy[i]
    if l != r:
        lazy[2*i+1] += lazy[i]
        lazy[2*i+2] += lazy[i]
    lazy[i] = 0

# Update [ul, ur] by val
def update(i, l, r, ul, ur, val):
    # Complete any lazy update since you're visiting that node
    lazyUpdate(i, l, r)

    # No overlap
    if r < ul or l > ur:
        return 
    
    # Complete overlap
    if ul <= l and r <= ur:
        tree[i] += (r-l+1)*val
        # Propage the value to children since you'll not be visiting them
        if l != r:
            lazy[2*i+1] += val
            lazy[2*i+2] += val
        return
    
    # Partial overlap
    mid = l+(r-l)//2
    update(2*i+1, l, mid, ul, ur, val)
    update(2*i+2, mid+1, r, ul, ur, val)
    tree[i] = tree[2*i+1] + tree[2*i+2]

def query(i, l, r, ql, qr):
   # Complete any lazy update since you're visiting that node
    lazyUpdate(i, l, r)

    # No overlap
    if r < ql or l > qr:
        return 0

    # Complete overlap
    if ql <= l and r <= qr:
        return tree[i]

    # Partial overlap
    mid = l+(r-l)//2
    lst = query(2*i+1, l, mid, ql, qr)
    rst = query(2*i+2, mid+1, r, ql, qr)
    return lst+rst