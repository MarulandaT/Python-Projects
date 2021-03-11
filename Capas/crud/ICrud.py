from abc import ABC, abstractmethod

class ICrud(ABC): 
	
	@abstractmethod
	def buscar_hospital (self, name): 
		raise NotImplementedError

	@abstractmethod
	def buscar_doctor (self, dni): 
		raise NotImplementedError

	@abstractmethod
	def relacion ( self , uno , muchos ):
		raise NotImplementedError