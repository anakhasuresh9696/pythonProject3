class Number:
	def __init__(self,Atomic_number,Atomic_mass_number):
	    self.Z = Atomic_number
	    self.A = Atomic_mass_number


def nuclearNotation(self):
	N=self.A-self.Z #N is Neutron number


print("total neutron number :")
Z= int(input("enter Atomic number : "))
A= int(input("enter Atomicmass : "))
N=int(input("enter Neutron number"))

s1 = Number(Z,A)
print("total neutron : ", s1.NuclearNotation())



