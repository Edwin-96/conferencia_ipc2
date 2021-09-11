class Nodo:
	def __init__(self, data, sig = None, pre = None):
		self.data = data
		self.sig = sig
		self.pre = pre

	def conectar(self, sig = None, pre = None):
		self.sig = sig
		self.pre = pre
		return self
	
	def conectar_sig(self, sig):
		self.sig = sig
		return self

	def conectar_pre(self, pre):
		self.pre = pre
		return self;

	def __gt__ (self, x):
		self.sig = x
		return self

	def __lt__ (self, x):
		x.pre = self
		return x


#Lista circular diblemente enlazada
class Lista:
	
	def __init__(self):
		self.inicio = None
		self.cantidad = 0
	
	#agrega al final
	def agregar(self, data):
		nuevoNodo = Nodo(data)
		if self.vacio(): self.inicio = nuevoNodo.conectar(nuevoNodo, nuevoNodo)
		else:
			nuevoNodo.conectar(self.inicio, self.inicio.pre)
			self.inicio.pre.conectar_sig(nuevoNodo)
			self.inicio.conectar_pre(nuevoNodo)
		self.cantidad += 1
		return True

	def add(self, data):
		nuevoNodo = Nodo(data)
		if self.vacio(): self.inicio = nuevoNodo < nuevoNodo > nuevoNodo
		else:
			self.inicio.pre < nuevoNodo > self.inicio
			self.inicio.pre > nuevoNodo
			nuevoNodo < self.inicio
		self.cantidad += 1
		return True

	# def agregar_si(self, data, condicion):
	# 	nuevoNodo = Nodo(data)
	# 	if self.vacio() and condicion(None): 
	# 		self.inicio = nuevoNodo.conectar(nuevoNodo, nuevoNodo)
	# 		self.cantidad += 1
	# 		return True
	# 	else:
	# 		aux = self.inicio
	# 		for i in range(0, self.cantidad):
	# 			if condicion(aux.data):					
	# 				nuevoNodo.conectar(aux.sig, aux.pre)
	# 				aux.conectar_sig(nuevoNodo)
	# 				aux.pre.conectar_pre(nuevoNodo)
	# 				self.cantidad += 1
	# 				return True
	# 			aux = aux.sig

	#elimina el ultimo dato ingresado
	def eliminar(self):
		if not self.vacio():
			self.cantidad -= 1
			if self.inicio == self.inicio.sig:
				data = self.inicio.data
				self.inicio = None
				return data
			else:
				ultimo = self.inicio.pre
				self.inicio.conectar_pre(ultimo.pre)
				ultimo.pre.sig.conectar_sig(self.inicio)
				return ultimo.data
	
	def eliminar_si(self, condicion):
		if not self.vacio():
			if self.inicio == self.inicio.sig and condicion(self.inicio.data):
				data = self.inicio.data
				self.inicio = None
				self.cantidad -= 1
				return data
			else:
				aux = self.inicio
				for i in range(0, self.cantidad):
					if condicion(aux.data):
						aux.pre.conectar_sig(aux.sig)
						aux.sig.conectar_pre(aux.pre)
						if aux == self.inicio: self.inicio = aux.sig
						self.cantidad -= 1
						return aux.data
					aux = aux.sig

	
	def ordenar(self, condicion):
		if not self.vacio():
			aux = self.inicio
			for i in range(0, self.cantidad):
				aux_i = aux.sig
				while aux_i != self.inicio:
					if condicion(aux.data, aux_i.data):
						aux_d = aux_i.data
						aux_i.data = aux.data
						aux.data = aux_d
					aux_i = aux_i.sig
				aux = aux.sig
		return None
	
	def recorrer(self, accion):
		if not self.vacio():
			aux = self.inicio
			for i in range(0, self.cantidad):
				accion(aux.data)
				aux = aux.sig

	def vacio(self):
		return self.cantidad == 0


def main():
	lista = Lista()	
	lista.agregar(3)
	lista.agregar(8)
	lista.agregar(5)
	lista.agregar(2)

	lista.add(10)
	lista.add(12)
	lista.add(19)
	#lista.eliminar_si(lambda item: item == 8)
	#lista.ordenar(lambda n1, n2: n1 > n2 )
	lista.recorrer(lambda item: print(item))



if __name__ == "__main__":main()
