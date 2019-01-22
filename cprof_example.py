import numpy as np
from numpy.linalg import eigvals

#@profile
def run_experiment(niter=100):
    K = 100
    results = []
    for _ in xrange(niter):
        mat = np.random.randn(K, K)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)

    return results

def fun():
    print(1)
    print(2)
    print(3)


some_results = run_experiment()
print('Laregest one we saw %s' % np.max(some_results))
print(111224)
ax = 10


