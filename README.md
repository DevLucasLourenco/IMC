# IMC

## Explicação:

Para a criação deste algoritmo, utilizei a boa prática de classes, juntamente de seus atributos, métodos e instância. Não foi necessário a utilização de polimorfismo ou paralelismo.
Levando em conta a alta capacidade do python em trabalhar com `garbage collection`, não me preocupei em tratar os dados alocados à memória.


Desenvolvi somente 6 métodos para o total funcionamento do código e irei explicá-lo a seguir:
- `__init__`
> Como temos em mente, o __init__ é um método mágico, tal como `__enter__`, `__name__`, e etc, cujo objetivo é executar as funções a partir do momento em que for instanciado.Nele, aloquei os atributos que seriam utilizados posteriormente no código, juntamente à ordem que planejei serem executadas as funções.

- `adaptar_altura` (@staticmethod)
> Este método, assim como as boas práticas uso de um @staticmethod, transcrito na PEP-257, serve somente para um único objetivo, receber um item e modificá-lo, sendo possível que o usuário passe qualquer formato de altura (ex.: 1.80 - 1,80 ou 180). Após receber o valor, será tratado e retornará a altura tratada.

- `receber_dados`
> Para este, sua única função é receber os dados do usuário através de uma list comprehension, sendo eles: Peso e Altura. Após recebê-los, é possívelr realizar o cálculo de IMC com a função seguinte.

- `calcular_imc`
> Esta função é utilizada para, através do recebimento do peso e altura, aplicar o cálculo. Para aplicar o cálculo, utilizei uma Lambda Expression(lambda a, b: a / pow(b, 2)). 

- `verificacao`
> Esta foi a maior função – em questão de tamanho – que eu desenvolvi para este projeto. Nela, preparei uma lógica onde irá perceber o valor calculado pela função de cálculo de IMC, interpretar e atribuir à tabela de classificação de IMC.

- `__table_initializer`
> Por fim, esta função serve de apoio à função acima, `verificação`. Ela é utilizada para criar a tabela a qual será tratada de acordo com o cálculo.



## Execução
 Para a execução do código, basta chamar uma instância do mesmo, afinal, no método mágico `__init__`, já performei todo o código de maneira apropriada para qual bastasse chamar uma instância e tudo ja seria executado.

```python

instancia = IMC()

```
A partir deste ponto, o código debugará e executará suas funcionalidades, cabendo o usuário responder aos inputs.


## libs
Para a realização do mesmo, utilizei somente duas `libs`. Seriam elas:
- `math`
- `beautifultable`


