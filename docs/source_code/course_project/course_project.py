import materials as m
from math import *
import numpy


print ('Stringer')
print('''
__________________________________
__________________________________  обшивка
_______                    _______  "ножка"
_______                    _______  низ стрингера
       |                  |         стенка стрингера
       |                  |       
       |__________________|         верх стрингера
       ____________________         "шляпка"''')

print('')
print('')

m.load_var(0)

mu12 = m.mu12
mu21 = m.E2/m.E1*mu12 		#приведенные фмх материала
E1p = m.E1/(1-mu12*mu21)
E2p = m.E2/(1-mu12*mu21)

#	Геом параметры панели
a = 140
b = 140

#Перепад температур
gradT = -50

'''структура обшивки в градусах и кол-во слоев'''
struct_plat_deg = [90, 45,-45, -45, 45, 90]
struct_plat = [i*pi/180 for i in struct_plat_deg]
struct_plat_n = [1, 1, 1, 1, 1, 1]

'''нижнего заплечика, или ножки'''
struct_down_deg = [0]
struct_down = [i*pi/180 for i in struct_down_deg]
struct_down_n = [0]

#	Ширина ножки стрингера и подставки стрингера
b_domw = 20

'''стрингера'''
struct_str_deg = [0]
struct_str = [i*pi/180 for i in struct_str_deg]
struct_str_n = [6]

#ширина верхнего заплечика или верха стрингера
b_up = 20

'''верхнего заплечника. или шляпки'''
struct_up_deg = [0]
struct_up = [i*pi/180 for i in struct_up_deg]
struct_up_n = [0]

'''высота в мм стенки стрингера. только стенки. без нижней кромки и верхней'''
h_str = 10

'''структура "условной слоистой системы" в градусах'''
struct_cond_deg = struct_plat_deg+struct_down_deg+struct_str_deg+struct_str_deg+struct_str_deg+struct_up_deg
'''в радианах'''
struct_cond = struct_plat+struct_down+struct_str+struct_str+struct_str+struct_up_deg
'''количество слоев каждой группы слоев "слоистой системы"'''
struct_cond_n = struct_plat_n+struct_down_n+struct_str_n+[1]+struct_str_n+struct_up_n
'''толщина каждой группы в мм'''
struct_cond_d = [i*m.d_0 for i in struct_plat_n]+[i*m.d_0 for i in struct_down_n]+[i*m.d_0 for i in struct_str_n]+[h_str]+[i*m.d_0 for i in struct_str_n]+[i*m.d_0 for i in struct_up_n]
print('структура "условной слоистой системы" в градусах', struct_cond_deg)
print('структура "условной слоистой системы" в радианах', struct_cond)
print('количество слоев каждой группы слоев "слоистой системы"', struct_cond_n)
print('толщина каждой группы в мм', struct_cond_d)

zi = []
spec_koef_kotoruj_bolshe_nigde_ne_nugen = 0
zi_minus_1 = []
for i in range(len(struct_cond_d)):
	zi_minus_1.append(spec_koef_kotoruj_bolshe_nigde_ne_nugen)
	spec_koef_kotoruj_bolshe_nigde_ne_nugen += struct_cond_d[i]
	zi.append(spec_koef_kotoruj_bolshe_nigde_ne_nugen)

print('zi   ===> ', zi)
print('zi-1 ===>    ', zi_minus_1)


'''всего слоев в пакете'''
n = 0
for i in range (len(struct_cond_n)):
	n += struct_cond_n[i]
print('всего слоев в пакете', n)

b11 = []
b12 = []
b13 = []
b22 = []
b23 = []
b33 = []

at1 = []
at2 = []
at3 = []

'''	
										Ввести массив редукционных элементов
'''
#red_k = [1 for i in struct_cond_deg]
red_k = [1 for i in struct_plat_n] + [b_domw*2/b for i in struct_down_n] + [b_domw*2/b for i in struct_str_n] + [2*struct_str_n[0]*m.d_0/b for i in struct_str_n] + [b_up/b for i in struct_str_n] + [b_up/b for i in struct_up_n]
print('Редуционные коэффициенты', red_k)


for i in range(len(struct_cond)):
	b11i = (E1p*cos(struct_cond[i])**4+2*E1p*mu21*sin(struct_cond[i])**2*cos(struct_cond[i])**2+E2p*sin(struct_cond[i])**4+m.G12*sin(2*struct_cond[i])**2)*red_k[i]
	b12i = ((E1p+E2p)*sin(struct_cond[i])**2*cos(struct_cond[i])**2+E1p*mu21*(sin(struct_cond[i])**4+cos(struct_cond[i])**4)-m.G12*sin(2*struct_cond[i])**2)*red_k[i]
	b13i = (sin(struct_cond[i])*cos(struct_cond[i])*(E1p*(1-mu21)*cos(struct_cond[i])**2-E2p*(1-mu12)*sin(struct_cond[i])**2-2*m.G12* cos(2*struct_cond[i])))*red_k[i]
	b22i = (E1p*sin(struct_cond[i])**4+2*E1p*mu21*sin(struct_cond[i])**2*cos(struct_cond[i])**2+E2p*cos(struct_cond[i])**4+m.G12*sin(2*struct_cond[i])**2)*red_k[i]
	b23i = (sin(struct_cond[i])*cos(struct_cond[i])*(E1p*(1-mu21)*sin(struct_cond[i])**2-E2p*(1-mu12)*cos(struct_cond[i])**2+2*m.G12* cos(2*struct_cond[i])))*red_k[i]
	b33i = ((E1p+E2p-2*E1p*mu21)*sin(struct_cond[i])**2*cos(struct_cond[i])**2+m.G12*cos(2*struct_cond[i])**2)*red_k[i]

	at1i = b11i*m.a1+b12i*m.a2
	at2i = b12i*m.a1+b22i*m.a2
	at3i = b13i*m.a1+b23i*m.a2

	'''at1i = (m.a1*E1p*(cos(struct_cond[i])**2+mu21*sin(struct_cond[i])**2)+m.a2*E2p*(sin(struct_cond[i])**2+mu12*cos(struct_cond[i])))*red_k[i]
		at2i = (m.a1*E1p*(sin(struct_cond[i])**2+mu21*cos(struct_cond[i])**2)+m.a2*E2p*(cos(struct_cond[i])**2+mu12*sin(struct_cond[i])))*red_k[i]
		at3i = (sin(struct_cond[i])*cos(struct_cond[i])*(m.a1*E1p*(1-mu21)-m.a2*E2p*(1-mu12)))*red_k[i]
	'''

	b11.append(b11i)
	b12.append(b12i)
	b13.append(b13i)
	b22.append(b22i)
	b23.append(b23i)
	b33.append(b33i)

	at1.append(at1i)
	at2.append(at2i)
	at3.append(at3i)

B11, B12, B13, B22, B23, B33 = 0, 0, 0, 0, 0, 0
C11, C12, C13, C22, C23, C33 = 0, 0, 0, 0, 0, 0
D11, D12, D13, D22, D23, D33 = 0, 0, 0, 0, 0, 0
Bt1, Bt2, Bt3, Dt1, Dt2, Dt3 = 0, 0, 0, 0, 0, 0

for i in range(len(struct_cond_d)):
	B11 += b11[i]*struct_cond_d[i]
	C11 += b11[i]*(zi[i]**2-zi_minus_1[i]**2)
	D11 += b11[i]*(zi[i]**3-zi_minus_1[i]**3)
	
	Bt1 += at1[i]*struct_cond_d[i]*gradT
	Dt1 += at1[i]*(zi[i]**2-zi_minus_1[i]**2)*gradT

for i in range(len(struct_plat)):
	B12 += b11[i]*struct_cond_d[i]
	B13 += b13[i]*struct_cond_d[i]
	B22 += b22[i]*struct_cond_d[i]
	B23 += b23[i]*struct_cond_d[i]
	B33 += b33[i]*struct_cond_d[i]
	Bt2 += at2[i]*struct_cond_d[i]*gradT
	Bt3 += at3[i]*struct_cond_d[i]*gradT

	C12 += b12[i]*(zi[i]**2-zi_minus_1[i]**2)
	C13 += b13[i]*(zi[i]**2-zi_minus_1[i]**2)
	C22 += b22[i]*(zi[i]**2-zi_minus_1[i]**2)
	C23 += b23[i]*(zi[i]**2-zi_minus_1[i]**2)
	C33 += b33[i]*(zi[i]**2-zi_minus_1[i]**2)

	D12 += b12[i]*(zi[i]**3-zi_minus_1[i]**3)
	D13 += b13[i]*(zi[i]**3-zi_minus_1[i]**3)
	D22 += b22[i]*(zi[i]**3-zi_minus_1[i]**3)
	D23 += b23[i]*(zi[i]**3-zi_minus_1[i]**3)
	D33 += b33[i]*(zi[i]**3-zi_minus_1[i]**3)

	Dt2 += at2[i]*(zi[i]**2-zi_minus_1[i]**2)*gradT
	Dt3 += at3[i]*(zi[i]**2-zi_minus_1[i]**2)*gradT

'''Узнать, почему для Дт з в квадрате, а не в кубе'''

B = B11*B22*B33+2*B12*B13*B23-B11*B12**2-B22*B13**2-B33*B12**2
B11p = (B22*B33-B23**2)/B
B12p = (B13*B23-B12*B33)/B
B13p = (B12*B23-B13*B22)/B
B22p = (B11*B33-B13**2)/B
B23p = (B12*B13-B11*B12)/B
B33p = (B11*B22-B12**2)/B


Bij_p = [  [B11p, B12p, B13p],
		   [B12p, B22p, B23p],
		   [B13p, B23p, B33p]   ]

Bti = [Bt1, Bt2, Bt3]

Cij = [  [C11, C12, C13],
		 [C12, C22, C23],
		 [C13, C23, C33]   ]

Dij = [  [D11, D12, D13],
		 [D12, D22, D23],
		 [D13, D23, D33]   ]

Dti = [Dt1, Dt2, Dt3]

Pij = [[0 for j in range(3)] for i in range(3)]
Pti = [0 for i in range(3)]

for k in range(3):
	for j in range(3):
		for i in range(3):
			Pij[k][j] += Cij[j][i]*Bij_p[i][k]

for k in range(3):
	for i in range(3):
		Pti[k] += Bti[i]*Bij_p[i][k]

Dij_p = Dij[:]

for k in range(3):
	for j in range(3):
		for i in range(3):
			Dij_p[k][j] -= Cij[k][i]*Pij[i][j]

Dti_p = Dti[:]

for k in range(3):
	for i in range(3):
		Dti_p[k] -= Cij[k][i]*Pti[i]

det_Dij_p = numpy.linalg.det(Dij_p)
#print(det_Dij_p)

proverka_opredelitela = Dij_p[0][0]*Dij_p[1][1]*Dij_p[2][2]  +  Dij_p[0][1]*Dij_p[1][2]*Dij_p[2][0]  +  Dij_p[0][2]*Dij_p[1][0]*Dij_p[2][1]  -  Dij_p[0][2]*Dij_p[1][1]*Dij_p[2][0]  -  Dij_p[0][1]*Dij_p[1][0]*Dij_p[2][2]  -  Dij_p[0][0]*Dij_p[1][2]*Dij_p[2][1]
#print(proverka_opredelitela)

mat_Dt_D_D = [[0 for i in range(3)] for j in range(3)]
mat_D_Dt_D = [[0 for i in range(3)] for j in range(3)]
mat_D_D_Dt = [[0 for i in range(3)] for j in range(3)]

for i in range(3):
	for j in range(3):
		if j == 0:
			mat_Dt_D_D[i][j] = Dti_p[i]
		else:
			mat_Dt_D_D[i][j] = Dij_p[i][j]

for i in range(3):
	for j in range(3):
		if j == 1:
			mat_D_Dt_D[i][j] = Dti_p[i]
		else:
			mat_D_Dt_D[i][j] = Dij_p[i][j]

for i in range(3):
	for j in range(3):
		if j == 2:
			mat_D_D_Dt[i][j] = Dti_p[i]
		else:
			mat_D_D_Dt[i][j] = Dij_p[i][j]

'''m.print_ar('Dt', Dti_p, '', 4)
m.print_result('Dijp', Dij_p, '')
print('')
m.print_result('mat_Dt_D_D', mat_Dt_D_D, '')
print('')
m.print_result('mat_D_Dt_D', mat_D_Dt_D, '')
print('')
m.print_result('mat_D_D_Dt', mat_D_D_Dt, '')'''

det_Dt_D_D = numpy.linalg.det(mat_Dt_D_D)
det_D_Dt_D = numpy.linalg.det(mat_D_Dt_D)
det_D_D_Dt = numpy.linalg.det(mat_D_D_Dt)

Kx =  det_Dt_D_D/det_Dij_p
Ky =  det_D_Dt_D/det_Dij_p
Kxy = det_D_D_Dt/det_Dij_p

print('Kx  = ', Kx)
print('Ky  = ', Ky)
print('Kxy = ', Kxy)

x = 70
y_str = 20
y = 40
C1, C2 = 0, 0
print('')
Wx = Kx*x**2/2
Wy_str = Ky*y_str**2/2
print("Wx = ", Wx)
print('Wy_str = ', Wy_str)
gamma = Ky*y_str
Wy = Wy_str+(y-y_str)*sin(gamma)
print('Wy = ', Wy)