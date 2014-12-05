from .polynomials cimport MultivariatePolynomial
from .riemann_surface_path cimport RiemannSurfacePathPrimitive

cdef class Differential:
    cdef object RS
    cdef object x
    cdef object y
    cdef object _omega
    cdef MultivariatePolynomial numer
    cdef MultivariatePolynomial denom
    cpdef complex eval(self, complex, complex)
    cpdef complex[:] evaluate(self, RiemannSurfacePathPrimitive, double[:])
