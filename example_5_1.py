from numpy import *

def solver(u, cells, rho, Gamma, L, phi_A, phi_B):
	F = rho*u
	dx = L/cells
	D = Gamma/dx
	aw = zeros(cells)
	ae = zeros(cells)
	Sp = zeros(cells)
	Su = zeros(cells)
	ap = zeros(cells)
	aw[1:] = D + F/2
	ae[0:-1] = D - F/2
	Sp[0] = -(2*D + F)
	Sp[-1] = -(2*D - F)
	Su[0] = (2*D + F)*phi_A
	Su[-1] = (2*D - F)*phi_B
	ap = aw + ae - Sp
	M = diagflat(ap) + diag(-aw[1:], -1) + diag(-ae[:-1], 1)
	phi = linalg.tensorsolve(M, Su)
	print phi

def exact_solution(rho, phi_A, phi_B):
	return 0

def main(rho, Gamma, L, phi_A, phi_B):
	#case1
	solver(0.1, 5, rho, Gamma, L, phi_A, phi_B)
	#case2
	solver(2.5, 5, rho, Gamma, L, phi_A, phi_B)
	#case3
	solver(2.5, 20, rho, Gamma, L, phi_A, phi_B)

main(1., 0.1, 1., 1., 0.)