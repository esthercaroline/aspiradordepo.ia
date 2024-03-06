from aigyminsper.search.SearchAlgorithms import BuscaCustoUniforme, BuscaLargura, BuscaProfundidade
from aigyminsper.search.Graph import State
import json



class U2(State):

    def __init__(self, op, bono, edge, adam, larry,lanterna, cost):
        # You must use this name for the operator!
        self.operator = op
        # Lado inicial todos False
        # Lado final todos True
        self.bono = bono
        self.edge = edge
        self.adam = adam
        self.larry = larry
        self.lanterna = lanterna
        self.cost_ = cost
    
    def successors(self):
        successors = []
        # bono para direita
        if self.bono == False and self.lanterna == False:
            s1 = U2('bono_dir', True, self.edge, self.adam, self.larry, True, 1)
            successors.append(s1)

        # edge para direita
        if self.edge == False and self.lanterna == False:
            s2 = U2('edge_dir', self.bono, True, self.adam, self.larry, True, 2)
            successors.append(s2)
        
        # adam para direita
        if self.adam == False and self.lanterna == False:
            s3 = U2('adam_dir', self.bono, self.edge, True, self.larry, True, 5)
            successors.append(s3)
        
        # larry para direita
        if self.larry == False and self.lanterna == False:
            s4 = U2('larry_dir', self.bono, self.edge, self.adam, True, True, 10)
            successors.append(s4)

        # bono para esquerda
        if self.bono == True and self.lanterna == True:
            s5 = U2('bono_esq', False, self.edge, self.adam, self.larry, False, 1)
            successors.append(s5)

        # edge para esquerda
        if self.edge == True and self.lanterna == True:
            s6 = U2('edge_esq', self.bono, False, self.adam, self.larry, False, 2)
            successors.append(s6)
        
        # adam para esquerda
        if self.adam == True and self.lanterna == True:
            s7 = U2('adam_esq', self.bono, self.edge, False, self.larry, False, 5)
            successors.append(s7)

        # larry para esquerda
        if self.larry == True and self.lanterna == True:
            s8 = U2('larry_esq', self.bono, self.edge, self.adam, False, False, 10)
            successors.append(s8)

        # bono e edge para direita
        if self.bono == False and self.edge == False and self.lanterna == False:
            s9 = U2('bono_edge_dir', True, True, self.adam, self.larry, True, 2)
            successors.append(s9)
        
        # bono e adam para direita
        if self.bono == False and self.adam == False and self.lanterna == False:
            s10 = U2('bono_adam_dir', True, self.edge, True, self.larry, True, 6)
            successors.append(s10)
        
        # bono e larry para direita
        if self.bono == False and self.larry == False and self.lanterna == False:
            s11 = U2('bono_larry_dir', True, self.edge, self.adam, True, True, 11)
            successors.append(s11)

        # bono e edge para esquerda
        if self.bono == True and self.edge == True and self.lanterna == True:
            s12 = U2('bono_edge_esq', False, False, self.adam, self.larry, False, 2)
            successors.append(s12)

        # bono e adam para esquerda
        if self.bono == True and self.adam == True and self.lanterna == True:
            s13 = U2('bono_adam_esq', False, self.edge, False, self.larry, False, 6)
            successors.append(s13)

        # bono e larry para esquerda
        if self.bono == True and self.larry == True and self.lanterna == True:
            s14 = U2('bono_larry_esq', False, self.edge, self.adam, False, False, 11)
            successors.append(s14)

        # edge e adam para direita
        if self.edge == False and self.adam == False and self.lanterna == False:
            s15 = U2('edge_adam_dir', self.bono, True, True, self.larry, True, 7)
            successors.append(s15)

        # edge e larry para direita
        if self.edge == False and self.larry == False and self.lanterna == False:
            s16 = U2('edge_larry_dir', self.bono, True, self.adam, True, True, 12)
            successors.append(s16)

        # edge e adam para esquerda
        if self.edge == True and self.adam == True and self.lanterna == True:
            s17 = U2('edge_adam_esq', self.bono, False, False, self.larry, False, 7)
            successors.append(s17)
        
        # edge e larry para esquerda
        if self.edge == True and self.larry == True and self.lanterna == True:
            s18 = U2('edge_larry_esq', self.bono, False, self.adam, False, False, 12)
            successors.append(s18)

        # adam e larry para direita
        if self.adam == False and self.larry == False and self.lanterna == False:
            s19 = U2('adam_larry_dir', self.bono, self.edge, True, True, True, 15)
            successors.append(s19)
        
        # adam e larry para esquerda
        if self.adam == True and self.larry == True and self.lanterna == True:
            s20 = U2('adam_larry_esq', self.bono, self.edge, False, False, False, 15)
            successors.append(s20)

        return successors
    
    def is_goal(self):
        return self.bono and self.edge and self.adam and self.larry and self.lanterna
    
    def description(self):
        return "Problema do U2"
    
    def cost(self):
        return self.cost_
    
    def env(self):
        return json.dumps(self.__dict__)

def main():
    estado_incial =  U2('', False, False, False, False, False, 0)
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(estado_incial, trace=False)
    if result != None:
        print('Achou!')
        # print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()