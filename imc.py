from math import pow
try:
    from beautifultable import BeautifulTable
except:
    print('Você não possui a lib BeautifulTable. Favor, relizar um "pip install beautifultable" no terminal.')



class IMC():
    
    def __init__(self):
        self.peso = None
        self.altura = None
        self.formula_calculada = None
        
        self._tabela_imc = {
                          0 : (18.5, 'Magreza 0'),
                          1 : (18.5, 'Normal 0'),
                          2 : (24.9, 'Sobrepeso I'),
                          3 : (29.9, 'Obesidade II'),
                          4 : (39.9, 'Obesidade Grave III'),
                          }
        
        self.table = BeautifulTable()
        
        self.__table_initializer()
        self.receber_dados()
        self.calcular_imc()
        self.verificacao()                      
    
    
    @staticmethod
    def adaptar_altura(item:str) -> float:
        item = str(item)
            
        if len(item) == 3:
            l1, l2, l3= [l for l in item]
            item_tratado = f'{l1}.{l2}{l3}'
            
            return float(item_tratado)

        elif ',' in item:
            item = item.replace(',','.')
            return float(item)
            
        
        elif '.' in item:
            return float(item)
        
        else:
            print(f'Valor {item} inválido.')
            raise ValueError 

    
    def receber_dados(self):
        pronome_possessivo = ['seu', 'sua']
        self.peso, self.altura = [input(f'Insira o {i+1}º dado: infome {pronome_possessivo[i]} {item}?') for i, item in enumerate(['peso','altura'])]
       
        
    def calcular_imc(self):
        formula = lambda a, b: a / pow(b, 2)
        
        self.peso = float(self.peso)
        self.altura = float(IMC.adaptar_altura(self.altura))
    
        self.formula_calculada = formula(self.peso, IMC.adaptar_altura(self.altura))
    
    
    def verificacao(self):
                
        textos = [f'Seu IMC é de { self.formula_calculada:.2f}', 'Atenção à análise:']
        textos = list(map(str.upper, textos))
        
        print('\n'.join(textos))
        
        if self.formula_calculada < self._tabela_imc[0][0]:

            self.table.rows[1]['Status'] = f'X - {self.formula_calculada:.2f}'
            print(self.table)
        
        elif self.formula_calculada >= self._tabela_imc[1][0] and self.formula_calculada < self._tabela_imc[3][0]:

            self.table.rows[2]['Status'] = f'X - {self.formula_calculada:.2f}'
            print(self.table)
            
        elif self.formula_calculada >= self._tabela_imc[2][0] and self.formula_calculada < self._tabela_imc[4][0]:

            self.table.rows[3]['Status'] = f'X - {self.formula_calculada:.2f}'
            print(self.table)
            
        elif self.formula_calculada >= self._tabela_imc[3][0] and self.formula_calculada < self._tabela_imc[5][0]:

            self.table.rows[4]['Status'] = f'X - {self.formula_calculada:.2f}'
            print(self.table)
            
        elif self.formula_calculada >= self._tabela_imc[4][0]:
            
            self.table.rows[5]['Status'] = f'X - {self.formula_calculada:.2f}'
            print(self.table)
    
    
    def __table_initializer(self):
        self.table.set_style(BeautifulTable.STYLE_BOX_DOUBLED)

        self.table.column_headers = ['IMC','Classificação', 'Status']
        for imc_valores, classificacao in self._tabela_imc.values():
            self.table.rows.append([imc_valores, classificacao, ''])
                    
    
    
if __name__ =='__main__':
    instancia = IMC()