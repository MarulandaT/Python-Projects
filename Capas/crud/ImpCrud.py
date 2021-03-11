from database import gestor
from crud import ICrud

class Crud( ICrud.ICrud ) : 

    def buscar_doctor (self, dni):
        return gestor.buscar_medico(dni)

    def buscar_hospital (self, nombre): 
        param = (str(nombre),)
        return gestor.buscar_hospital(param)

    def relacion (self, uno, muchos): 
        uno.doctores = muchos 
        return uno
