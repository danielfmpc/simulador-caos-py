import random
import seaborn as sns
class Academia:
  def __init__(self):
    self.halteres = [i for i in range(10, 36) if i % 2 == 0]
    self.porta_halteres = {}
    self.reiniciar_o_dia()

  def reiniciar_o_dia(self):
    self.porta_halteres = {i: i for i in self.halteres}

  def listar_halteres(self):
    return [i for i in self.porta_halteres.values() if i != 0]

  def pegar_alteres(self, peso):
    halter_pos = list(self.porta_halteres.values()).index(peso)
    key_halter = list(self.porta_halteres.keys())[halter_pos]
    self.porta_halteres[key_halter] = 0

  def devolver_halter(self, peso):
    self.porta_halteres[peso] = peso

  def listar_espacos(self):
    return [i for i, j in self.porta_halteres.items() if j == 0] 

  def calcular_caos(self):
    num_caos = [i for i, j in self.porta_halteres.items() if i != j]
    return len(num_caos) / len(self.porta_halteres)

class Usuario:
  def __init__(self, tipo, academia):
    self.tipo = tipo
    self.academia = academia
    self.peso = 0

  def iniciar_treino(self):
    lista_peso = self.academia.listar_halteres()
    self.peso = random.choice(lista_peso)
    self.academia.pegar_alteres(self.peso)

  def finalizar_treino(self):
    espacos = self.academia.listar_espacos()
    if self.tipo == 1:
      if self.peso in espacos:
        self.academia.devolver_halter(self.peso, self.peso)
      else:
        pos = random.choice(espacos)
        self.academia.devolver_halter(pos, self.peso)
    
    if self.tipo == 2:
      pos = random.choice(espacos)
      self.academia.devolver_halter(pos, self.peso)
    
    self.peso = 0

academia = Academia()
usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]
random.shuffle(usuarios)

list_caos = []
for k in list_caos:
  academia.reiniciar_o_dia()
  for i in range(10):
    random.shuffle(usuarios)
    for usuario in usuarios:
      usuario.iniciar_treino()
    for usuario in usuarios:
      usuario.finalizar_treino()
  list_caos += [academia.calcular_caos()]

print(academia.porta_halteres)
print(list_caos)

sns.displot(list_caos)