import random
import matplotlib.pyplot as plt
from scipy import integrate
import random 
import numpy as np

# Ejemplo: Aproximando el valor de pi - área de un círculo de
# radio = 1.
def mc_pi_aprox(N=100000):
    plt.figure(figsize=(10,10))  # tamaño de la figura
    x, y, z = np.random.uniform(-1, 1, size=(3, N))
    print(x)
    interior = (x**2 + y**2) <= 1
    print(interior)
    #Area circulo pi*r^2
    #Area cuadrado (2r)^2
    #Area_circulo/Area_cuadrado = pi/4  ==> pi = 4*n_dentro_del_circulo/N
    pi = interior.sum() * 4 / N
    error = abs((pi - np.pi) / pi) * 100
    exterior = np.invert(interior)
    plt.plot(x[interior], y[interior], 'b.')
    plt.plot(x[exterior], y[exterior], 'r.')
    plt.plot(0, 0, label='$\hat \pi$ = {:4.4f}\nerror = {:4.4f}%'
             .format(pi,error), alpha=0)
    plt.axis('square')
    plt.legend(frameon=True, framealpha=0.9, fontsize=16)
    plt.show()

#N° 3
class Exponencial:
    prom_mensual = 0
    inter = 1
    def __init__(self, _theta):
        self.theta = _theta

    def get_Data(self, n):
        self.data = []
        for i in range(n):
            self.data = np.append(self.data, -(np.log(1-random.random())/self.theta))

    def show(self, n):
        self.get_Data(n)
        print(self.data)
        _bins = np.arange(min(self.data), max(self.data) + self.inter, self.inter)
        plt.hist(self.data, bins = _bins)
        plt.show()

    def prom_Mes(self, dias, nombre):
        mes = 1
        prom = 0
        prom_prom = 0
        #prom_total
        f = open(nombre,'w')
        f.write("\n Mes: " + str(mes)+"\n")
        for data in range(len(self.data)):
            if(data != 0 and (data+1) % dias == 0 ):
                prom += int(self.data[data])
                f.write(str(int(self.data[data]))+ "\n")
                #print(mes)
                #print(prom/dias)
                f.write("Promedio mensual: " + str(prom/dias)+"\n")
                prom_prom += prom/dias
                prom = 0
                mes += 1
                if(mes <= len(self.data)/dias):
                    #print(len(self.data)/dias)
                    f.write("\n Mes: " + str(mes)+"\n")
                pass
            else:
                f.write(str(int(self.data[data]))+"\n")
                prom += int(self.data[data])
        n_meses = len(self.data)/dias
        self.prom_mensual = prom_prom/n_meses
        print(self.prom_mensual)
        f.write("\nPromedio de los promedios mensuales: "+str(self.prom_mensual))
        f.close()
        
def dens_Normal(x, prom, var):
    return (1/(var*np.sqrt(2*np.pi)))*np.exp(-(1/2)*((x-prom)/var)**2)

class Normal:
    prom_mensual = 0
    inter = 1
    def __init__(self, _prom, _var):
        self.prom = _prom
        self.var = _var

    def dist_Normal(self, a, b):
        return integrate.quad(dens_Normal, a, b, args=(self.prom, self.var))[0]

    def show(self, n):
        self.data = np.random.normal(self.prom, np.sqrt(self.var), n)
        print(self.data)
        _bins = np.arange(min(self.data), max(self.data) + self.inter, self.inter)
        plt.hist(self.data, bins = _bins)
        plt.show()
    
    def prom_Mes(self, dias, nombre):
        mes = 1
        prom = 0
        prom_prom = 0
        #prom_total
        f = open(nombre,'w')
        f.write("\n Mes: " + str(mes)+"\n")
        for data in range(len(self.data)):
            if(data != 0 and (data+1) % dias == 0 ):
                prom += int(self.data[data])
                f.write(str(int(self.data[data]))+ "\n")
                #print(mes)
                #print(prom/dias)
                f.write("Promedio mensual: " + str(prom/dias)+"\n")
                prom_prom += prom/dias
                prom = 0
                mes += 1
                if(mes <= len(self.data)/dias):
                    #print(len(self.data)/dias)
                    f.write("\n Mes: " + str(mes)+"\n")
                pass
            else:
                f.write(str(int(self.data[data]))+"\n")
                prom += int(self.data[data])
        n_meses = len(self.data)/dias
        self.prom_mensual = prom_prom/n_meses
        print(self.prom_mensual)
        f.write("\nPromedio de los promedios mensuales: "+str(self.prom_mensual))
        f.close()

#N° 2
def peso_cajas(dias):
    n_total_cajas = 0
    f = open("cajas.txt", "w")
    for d in range(dias):
        print("Día: "+str(d+1))
        f.write("Día: "+str(d+1)+"\n")
        for v in range(5):
            print("Viaje número: "+str(v+1))
            f.write("Viaje número: "+str(v+1)+"\n")
            peso_total = 0
            n_cajas = 0
            while(peso_total <= 435):
                caja = np.sqrt(-np.log(1-random.random()))*20 + 190
                if (peso_total + caja) <= 625:
                    peso_total +=caja
                    n_cajas +=1
                    print(caja)
                    f.write(str(caja)+"\n")
            print("N° de cajas: "+str(n_cajas)+" Peso Total: "+str(peso_total))
            f.write("N° de cajas: "+str(n_cajas)+" Peso Total: "+str(peso_total)+"\n")
            n_total_cajas += n_cajas
    f.write("Promedio total de cajas por día: "+str(n_total_cajas/dias))
    print("Promedio total: "+str(n_total_cajas/dias))
    f.close()

#N° 1
def gamma_ent(r):
    #para numeros enteros positivos
    fact = 1
    for i in range(1, int(r)+1):
        fact = fact * i
    return fact

def esp_integrand(x, r):
        return (x**(r-1))*np.exp(-x)

class Weibull:
    _inter = 0.01
    def __init__(self, _const, _alpha):
        self.const = _const
        self.alpha = _alpha
        self._Fx = lambda x: 1 - np.exp((-self.const*x)**self.alpha)
        self._data = []
    
    def get_Data(self, N):
        self._data = []
        for i in range(N):
            self._data = np.append(self._data, ((-np.log(1-random.random()))**(1/self.alpha))/self.const)

    def show(self, N):
        self.get_Data(N)
        print(self._data)
        _bins = np.arange(min(self._data), max(self._data) + self._inter, self._inter)
        plt.hist(self._data, bins = _bins)
        plt.show()

    def esperanza(self):
        r = (1 + 1/self.alpha)
        I = integrate.quad(esp_integrand, 0, np.inf, args=(r))
        return (1/self.const)*I[0]

    def promedio(self):
        return np.average(self._data)

    def confiabilidad(self, t):
        return np.exp(-(self.const*t)**self.alpha)

#1
#w = Weibull(3, 5)
#g = gamma(4)
#print(g)
#w.show(1000)
#print(w.esperanza())
#print(w.promedio())
#print(np.random.weibull(5, 1))
#print (w.confiabilidad(0))
#2
#peso_cajas(30)
#3
n1 = Normal(140, 16)
n1.show(3000)
n1.prom_Mes(30, "vent1.txt")

n2 = Normal(153, 14)
n2.show(3000)
n2.prom_Mes(30, "vent2.txt")

e = Exponencial(1/150)
e.show(3000)
e.prom_Mes(30, "vent3.txt")
