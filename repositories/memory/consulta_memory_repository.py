from models.consulta import Consulta

class ConsultaMemoryRepository:
    def __init__(self):
        self.consultas = {}
        self.proximo_id = 1
     
     
      #Salvar
    def save(self, consulta):
        consulta.id_consulta = self.proximo_id
        self.consultas[self.proximo_id] = consulta
        self.proximo_id += 1

        return consulta
     
     #Procurar pelo id
    def find_by_id(self, id_consulta):
        return self.consultas.get(id_consulta)
    
    #Listar todas as consultas
    def get_all(self):
        return list(self.consultas.values())

     #Atualizar consulta
    def update(self, consulta):
        if consulta.id_consulta not in self.consultas:
            return False

        self.consultas[consulta.id_consulta] = consulta
        return True

     #Excluir consulta
    def delete(self, id_consulta):
        if id_consulta not in self.consultas:
            return False

        del self.consultas[id_consulta]
        return True

            


if __name__ == "__main__":

    repositorio = ConsultaMemoryRepository()

    # Criando uma consulta
    consulta1 = Consulta(
        id_paciente=1,
        id_medico=2,
        data_hora="2026-11-05 14:30",
        diagnostico="Rotina",
        valor_consulta=150.0
    )

    # Testando o save
    repositorio.save(consulta1)
    print("Consulta salva:")
    print(consulta1.to_dict())

    # Testando o find_by_id
    print("\nBuscando consulta:")
    encontrada = repositorio.find_by_id(1)
    print(encontrada.to_dict())

    # Testando o get_all
    print("\nTodas as consultas:")
    for consulta in repositorio.get_all():
        print(consulta.to_dict())

    # Testando o update
    consulta1.diagnostico = "Retorno"
    atualizado = repositorio.update(consulta1)

    print("\nConsulta atualizada:")
    print("Atualizou?", atualizado)
    print(repositorio.find_by_id(1).to_dict())

    print("\nExcluindo consulta:")
excluiu = repositorio.delete(1)
print("Excluiu?", excluiu)

print("Consultas restantes:")
print(repositorio.get_all())
