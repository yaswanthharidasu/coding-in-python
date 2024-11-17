# for sum use case
a = [1, 2, 3, 4, 5, 6, 7, 8]
tree = [0]*4*len(a)

def build(i, l, r):
    if l == r:
        tree[i] = a[l]
    else:
        mid = l + (r-l)//2
        build(2*i+1, l, mid)
        build(2*i+2, mid+1, r)
        tree[i] = tree[2*i+1] + tree[2*i+2]

def query(i, l, r, ql, qr):
    # Complete overlap
    if ql <= l and r <= qr:
        return tree[i]
    # No overlap
    if qr < l or ql > r:
        return 0
    # Partial overlap
    mid = l + (r-l)//2
    lst = query(2*i+1, l, mid, ql, qr)
    rst = query(2*i+2, mid+1, r, ql, qr)
    return lst+rst
    
def update(i, l, r, newi, val):
    if l == r:
        tree[i] = val
    else:
        mid = l + (r-l)//2
        if newi <= mid:
            update(2*i+1, l, mid, newi, val)
        else:
            update(2*i+2, mid+1, r, newi, val)
        tree[i] = tree[2*i+1] + tree[2*i+2]

build(0, 0, len(a)-1)
print(query(0, 0, len(a)-1, 3, 5))
update(0, 0, len(a)-1, 4, 10)
print(query(0, 0, len(a)-1, 3, 5))
