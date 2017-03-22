def split_cells(x, fac):
    "Expand 2D numpy array x with factor fac."
    assert type(fac) is int
    
    n = x.shape[0]
    m = x.shape[1]
    
    a = np.zeros((fac * n, n))
    b = np.zeros((m, fac * m))
    
    for i in range(n):
        a[i * fac: (i + 1) * fac, i] = 1
        
    for i in range(m):
        b[i, i * fac: (i + 1) * fac] = 1
        
    split_x = a @ x @ b
    
    return split_x, a, b
