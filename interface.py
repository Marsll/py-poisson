import numpy as np
import pypoisson.create_laplacian as create_laplacian

epsilon = 0.3

rho = np.random.rand(100, 50)
rho -= np.mean(rho)
phi = create_laplacian.solve(rho, epsilon, h=[0.1, 0.2])

laplacian = create_laplacian.create_laplacian(phi.shape, h=[0.1, 0.2])
phi_ = phi.reshape(-1, 1)
rho_ = np.dot(laplacian, phi_)
rho_ = rho.reshape(rho.shape)
print(np.testing.assert_allclose(rho_, rho))
