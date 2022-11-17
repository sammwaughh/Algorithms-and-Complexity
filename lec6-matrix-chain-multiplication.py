# Optimal Matrix Chain Multiplications

# Top Down
p = [10,100,5,50]
n = len(p)-1

m = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(None)
    m.append(row)

def mM(m, p, i, j):
    if m[i][j] != None:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        q = None
        for k in range(i, j):
            if q != None:
                val = mM(m, p, i, k) + mM(m,p,k+1,j) + p[i-1]*p[k]*p[j]
                if val < q:
                    q = val
            else:
                q = mM(m, p, i, k) + mM(m,p,k+1,j) + p[i-1]*p[k]*p[j]
        m[i][j] = q
    return m[i][j]

print(mM(m, p, 0, n-1))

