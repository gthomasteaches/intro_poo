from modelo.naranja import Naranja
from modelo.canasta import Canasta


mi_naranja = Naranja("Mi otra granja", 1 )
print("La granja de mi naranja es ", mi_naranja.granja )
print("El peso de mi naranja es ", mi_naranja.obtener_peso(), "kg")
mi_canasta = Canasta() 
print("Mi canasta tiene ", mi_canasta.calcular_cantidad_de_naranjas(), "naranjas")
mi_naranja.recoger(mi_canasta)
print("Mi canasta tiene ", mi_canasta.calcular_cantidad_de_naranjas(), "naranjas")

