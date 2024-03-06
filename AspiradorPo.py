from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State


class AspiradorPo(State):

    def __init__(self, op, left_state, right_state):
        # You must use this name for the operator!
        self.operator = op
        self.robot_pos = ''
        self.left_state = left_state
        self.right_state = right_state
        self.clean = False
        #TODO
    
    def successors(self):
        successors = []
        #TODO
        return successors
    
    def is_goal(self):
        pass
    
    def description(self):
        return "Descrição do problema"
    
    def cost(self):
        return 1
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        return json.dumps(self.__dict__)

def main():
    print('Busca em profundidade iterativa')
    estado_incial =  AspiradorPo('', False, True, 'esq')
    algorithm = BuscaLargura()
    result = algorithm.search(estado_incial, trace=True)
    # algorithm = BuscaProfundidade()
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()