import numpy as np
import pypoisson.create_laplacian

rho = np.random.rand(100, 50)
rho -= np.mean(rho)
phi = solve(rho, epsilon=1.0, h=[0.1, 0.2])

laplacian = create_laplacian(phi.shape, h=[0.1, 0.2])
phi_ = phi.reshape(-1, 1)
rho_ = np.dot(laplacian, phi_)
rho_ = rho.reshape(rho.shape)
np.testing.assert_allclose(rho_, rho)
