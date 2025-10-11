# Algoritmo para Encontrar Caminho Hamiltoniano

Programa em Python que implementa o algoritmo para encontrar um Caminho Hamiltoniano em um grafo orientado ou não orientado.

## 📝 Descrição do Projeto

Um **Caminho Hamiltoniano** em um grafo é um caminho que visita cada vértice exatamente uma vez. Encontrar esse caminho é um problema clássico em teoria dos grafos e está associado a problemas de alta complexidade computacional, como o Problema do Caixeiro Viajante.

Este projeto implementa uma abordagem para determinar se um Caminho Hamiltoniano existe em um grafo e, em caso afirmativo, encontrá-lo utilizando algoritmo de **backtracking**.

### Algoritmo e Lógica Implementada

O algoritmo implementado utiliza a técnica de **backtracking** (retrocesso) para explorar sistematicamente todos os possíveis caminhos no grafo. A lógica principal está dividida nas seguintes funções:

#### Principais Funções:

1. **`_backtrack(vertice_atual, posicao)`**:
   - Função recursiva principal que implementa o algoritmo de backtracking
   - Marca o vértice atual como visitado
   - Verifica se todos os vértices foram visitados (condição de parada)
   - Explora recursivamente todos os vértices adjacentes não visitados
   - Desfaz as marcações quando não encontra solução (backtrack)

2. **`encontrar_caminho(vertice_inicial=None)`**:
   - Interface principal para buscar um caminho hamiltoniano
   - Permite especificar um vértice inicial ou tenta todos os vértices
   - Inicializa as estruturas de controle (visitados, caminho)
   - Retorna se encontrou um caminho e qual é o caminho

3. **`encontrar_todos_caminhos()`**:
   - Variação do algoritmo que encontra todos os caminhos hamiltonianos possíveis
   - Utiliza backtracking modificado para não parar no primeiro caminho encontrado
   - Útil para análise completa de grafos pequenos

#### Estruturas de Dados Utilizadas:

- **Matriz de Adjacência**: Representa as conexões do grafo de forma eficiente
- **Array de Visitados**: Controla quais vértices já foram visitados no caminho atual
- **Array do Caminho**: Armazena a sequência de vértices que formam o caminho hamiltoniano

## 🚀 Como Executar o Projeto

### Pré-requisitos

- **Python 3.6+** instalado no sistema
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão do Python)

### Instruções para Execução Local

1. **Clone ou baixe o repositório**:
   ```bash
   git clone https://github.com/ViniciusXR/FPAA_Caminho_Hamiltoniano.git
   cd FPAA_Caminho_Hamiltoniano
   ```

2. **Execute o programa principal**:
   ```bash
   python main.py
   ```

3. **Navegue pelo menu interativo**:
   - O programa apresentará um menu com 4 opções
   - Escolha a opção desejada digitando o número correspondente
   - Siga as instruções na tela para cada funcionalidade

### Opções Disponíveis:

- **Opção 1**: Criar grafo personalizado (permite definir vértices e arestas)
- **Opção 2**: Executar exemplos predefinidos (demonstra diferentes cenários)
- **Opção 3**: Testar grafo completo (testa grafos completos K_n)
- **Opção 4**: Sair do programa

### Exemplo de Execução:

```bash
PS C:\...\FPAA_Caminho_Hamiltoniano> python main.py

============================================================
ALGORITMO PARA ENCONTRAR CAMINHO HAMILTONIANO
============================================================

Opções:
1. Criar grafo personalizado
2. Executar exemplos predefinidos
3. Testar grafo completo
4. Sair

Escolha uma opção (1-4): 2
```

---

# 📊 Relatório Técnico - Análise do Algoritmo

## 1. Análise da Complexidade Computacional

### 1.1 Classes P, NP, NP-Completo e NP-Difícil

#### Classificação do Problema do Caminho Hamiltoniano:

O **Problema do Caminho Hamiltoniano** pertence à classe **NP-Completo**.

#### Justificativa:

**1. Pertence à classe NP:**
- **Verificação em tempo polinomial**: Dado um caminho candidato, podemos verificar se é hamiltoniano em O(n) tempo
- **Certificado verificável**: O caminho proposto serve como certificado que pode ser verificado eficientemente

**2. É NP-Completo:**
- **Redução do Problema do Ciclo Hamiltoniano**: O problema do Caminho Hamiltoniano pode ser reduzido ao Problema do Ciclo Hamiltoniano (conhecido como NP-Completo) adicionando um vértice conectado aos extremos do caminho
- **Redução para SAT**: Pode ser reduzido ao problema da Satisfabilidade Booleana (SAT), que é NP-Completo

**3. Relação com o Problema do Caixeiro Viajante (TSP):**
- O TSP é **NP-Difícil** (mais difícil que NP-Completo)
- O Caminho Hamiltoniano é um caso especial do TSP onde:
  - Não há pesos nas arestas
  - Não é necessário retornar ao vértice inicial
  - Se pudermos resolver TSP, podemos resolver Caminho Hamiltoniano
- Esta relação confirma que o Caminho Hamiltoniano está na fronteira da intratabilidade computacional

**Características das Classes:**
- **P**: Problemas solucionáveis em tempo polinomial deterministicamente
- **NP**: Problemas verificáveis em tempo polinomial não-deterministicamente
- **NP-Completo**: Problemas mais difíceis de NP (incluindo Caminho Hamiltoniano)
- **NP-Difícil**: Pelo menos tão difíceis quanto os problemas NP-Completos

### 1.2 Análise da Complexidade Assintótica de Tempo

#### Complexidade Temporal do Algoritmo: **O(n!)**

#### Método de Determinação - Contagem de Operações:

**1. Análise da Função de Recorrência:**
```
T(n) = número de chamadas recursivas × tempo por chamada

Para cada vértice não visitado:
- Máximo de (n-1) vértices adjacentes a explorar
- Em cada nível de recursão, temos menos vértices disponíveis
```

**2. Expansão Detalhada:**
```
Nível 0: n possibilidades (vértice inicial)
Nível 1: (n-1) possibilidades (vértices restantes)
Nível 2: (n-2) possibilidades
...
Nível (n-1): 1 possibilidade

Total de operações ≤ n × (n-1) × (n-2) × ... × 1 = n!
```

**3. Operações por Chamada Recursiva:**
- Marcar/desmarcar vértice como visitado: O(1)
- Verificar adjacências: O(n) no pior caso
- Verificar condição de parada: O(1)

**Fórmula da Recorrência:**
```
T(n) = T(n-1) + T(n-2) + ... + T(1) + O(n)
```

Que resolve para **T(n) = O(n!)**

### 1.3 Aplicação do Teorema Mestre

#### Verificação de Aplicabilidade:

**O Teorema Mestre NÃO é aplicável ao algoritmo do Caminho Hamiltoniano.**

#### Critérios de Aplicabilidade do Teorema Mestre:

O Teorema Mestre aplica-se a recorrências da forma:
```
T(n) = a × T(n/b) + f(n)
```

Onde:
- `a ≥ 1` (número de subproblemas)
- `b > 1` (fator de divisão do problema)
- `f(n)` (custo para dividir/combinar)

#### Por que NÃO se aplica ao nosso algoritmo:

1. **Não há divisão sistemática**: O problema não é dividido em subproblemas de tamanho n/b
2. **Número variável de subproblemas**: O número de chamadas recursivas varia conforme a estrutura do grafo
3. **Dependência do estado**: Cada chamada recursiva depende do estado atual (vértices visitados)
4. **Estrutura de árvore irregular**: A árvore de recursão não tem estrutura regular requerida pelo teorema

#### Alternativa de Análise:

Para problemas de backtracking como este, utilizamos:
- **Análise por árvore de recursão**
- **Contagem direta de operações**
- **Análise de casos (melhor, médio, pior)**

### 1.4 Análise dos Casos de Complexidade

#### 1.4.1 Pior Caso: **O(n!)**

**Cenário:**
- Grafo completo ou quase completo
- Caminho hamiltoniano existe apenas após explorar quase todas as possibilidades
- Ou não existe caminho hamiltoniano

**Características:**
```
- Explora todas as n! permutações possíveis
- Ocorre em grafos densos
- Tempo de execução: exponencial
```

**Exemplo:** Grafo completo K_n onde o caminho está na última posição testada

#### 1.4.2 Melhor Caso: **O(n)**

**Cenário:**
- Existe um caminho hamiltoniano que é encontrado imediatamente
- Grafo tem estrutura linear (caminho simples)

**Características:**
```
- Encontra solução na primeira tentativa
- Apenas uma sequência de vértices válida
- Tempo de execução: linear
```

**Exemplo:** Grafo linear: 0 → 1 → 2 → 3 → ... → (n-1)

#### 1.4.3 Caso Médio: **O(k × n!)** onde k < 1

**Cenário:**
- Comportamento típico em grafos aleatórios
- Poda significativa da árvore de busca

**Características:**
```
- Explora uma fração das possibilidades totais
- Depende da densidade e estrutura do grafo
- Beneficia-se de podas no backtracking
```

#### 1.4.4 Impacto no Desempenho:

**1. Escalabilidade:**
```
n = 10: ~3.6 milhões de operações (pior caso)
n = 15: ~1.3 trilhões de operações (pior caso)
n = 20: ~2.4 × 10^18 operações (pior caso)
```

**2. Limitações Práticas:**
- Viável para grafos pequenos (n ≤ 15)
- Impraticável para grafos grandes sem heurísticas
- Beneficia-se de técnicas de poda inteligente

**3. Otimizações Possíveis:**
- **Poda por grau**: Eliminar vértices com grau insuficiente
- **Ordenação heurística**: Priorizar vértices com menor grau
- **Paralelização**: Distribuir busca entre múltiplos processadores
- **Programação dinâmica**: Armazenar subproblemas já resolvidos (Held-Karp)

### Conclusão da Análise Técnica

O algoritmo implementado oferece uma solução exata para o Problema do Caminho Hamiltoniano, adequada para fins educacionais e grafos de tamanho pequeno a médio. A complexidade exponencial é uma limitação inerente ao problema (NP-Completo), não ao algoritmo específico, representando o estado da arte atual para soluções exatas deste tipo de problema.

**Principais Contribuições do Projeto:**
- Implementação didática e bem documentada do algoritmo de backtracking
- Análise completa de complexidade computacional
- Interface interativa para experimentação prática
- Exemplos demonstrativos de diferentes cenários
- Código modular e extensível para futuras melhorias

---

## 🚀 Funcionalidades do Programa

- ✅ Suporte para grafos **orientados** e **não orientados**
- ✅ Busca por **um caminho hamiltoniano**
- ✅ Busca por **todos os caminhos hamiltonianos** possíveis
- ✅ Interface **interativa** com menu
- ✅ **Exemplos predefinidos** para demonstração
- ✅ Criação de **grafos personalizados**
- ✅ Geração de **grafos completos**
- ✅ Representação por **matriz de adjacência**
- ✅ Visualização da estrutura do grafo

## 🏗️ Estrutura do Projeto

```
FPAA_Caminho_Hamiltoniano/
├── main.py          # Programa principal
├── README.md        # Documentação
└── LICENSE          # Licença do projeto
```

## 📋 Classes Principais

### `Grafo`
Classe para representar um grafo que pode ser orientado ou não orientado.

**Métodos principais:**
- `adicionar_aresta(origem, destino)` - Adiciona uma aresta
- `remover_aresta(origem, destino)` - Remove uma aresta
- `tem_aresta(origem, destino)` - Verifica se existe aresta
- `obter_adjacentes(vertice)` - Obtém vértices adjacentes
- `imprimir_grafo()` - Exibe representação do grafo

### `CaminhoHamiltoniano`
Classe que implementa o algoritmo de busca por caminhos hamiltonianos.

**Métodos principais:**
- `encontrar_caminho(vertice_inicial=None)` - Encontra um caminho hamiltoniano
- `encontrar_todos_caminhos()` - Encontra todos os caminhos hamiltonianos possíveis

## 🎯 Como Usar

### Execução Básica

```bash
python main.py
```

### Menu Interativo

O programa oferece um menu com as seguintes opções:

1. **Criar grafo personalizado** - Permite criar um grafo customizado
2. **Executar exemplos predefinidos** - Demonstra diferentes cenários
3. **Testar grafo completo** - Testa grafos completos K_n
4. **Sair** - Encerra o programa

### Exemplos de Uso

#### Exemplo 1: Criando um Grafo Personalizado

```python
# Criar um grafo não orientado com 4 vértices
grafo = Grafo(4, orientado=False)

# Adicionar arestas
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 0)

# Buscar caminho hamiltoniano
algoritmo = CaminhoHamiltoniano(grafo)
encontrou, caminho = algoritmo.encontrar_caminho()

if encontrou:
    print(f"Caminho encontrado: {' -> '.join(map(str, caminho))}")
else:
    print("Nenhum caminho hamiltoniano encontrado")
```

#### Exemplo 2: Grafo Orientado

```python
# Criar um grafo orientado
grafo = Grafo(3, orientado=True)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(1, 2)

algoritmo = CaminhoHamiltoniano(grafo)
encontrou, caminho = algoritmo.encontrar_caminho()
```

## 🧩 Algoritmo

O programa utiliza **algoritmo de backtracking** para encontrar caminhos hamiltonianos:

1. **Inicialização**: Marca todos os vértices como não visitados
2. **Recursão**: Para cada vértice atual:
   - Marca como visitado
   - Adiciona ao caminho atual
   - Se todos os vértices foram visitados → caminho encontrado
   - Senão, tenta todos os vértices adjacentes não visitados
3. **Backtrack**: Se não encontra solução, desfaz a escolha atual
4. **Repetição**: Tenta diferentes vértices como ponto de partida

### Complexidade
- **Tempo**: O(n!) no pior caso, onde n é o número de vértices
- **Espaço**: O(n) para armazenar o caminho e vértices visitados

## 📊 Exemplos Predefinidos

O programa inclui exemplos que demonstram diferentes cenários:

### Exemplo 1: Grafo com Caminho Hamiltoniano
```
Vértices: 5 (0, 1, 2, 3, 4)
Arestas: (0,1), (1,2), (2,3), (3,4), (1,3), (0,4)
Resultado: ✅ Múltiplos caminhos encontrados
```

### Exemplo 2: Grafo Orientado
```
Vértices: 4 (0, 1, 2, 3)
Arestas: (0→1), (1→2), (2→3), (0→3)
Resultado: ✅ Caminho: 0 → 1 → 2 → 3
```

### Exemplo 3: Grafo sem Caminho
```
Vértices: 4 (0, 1, 2, 3)
Arestas: (0,1), (2,3) [grafo desconectado]
Resultado: ❌ Nenhum caminho hamiltoniano
```

## 🔧 Requisitos

- **Python 3.6+**
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão)

## 🎨 Características do Código

- **Documentação completa** com docstrings
- **Tratamento de erros** robusto
- **Interface amigável** com menu interativo
- **Código modular** e reutilizável
- **Exemplos práticos** incluídos
- **Suporte a diferentes tipos** de grafo

## 📈 Possíveis Extensões

- Implementação de heurísticas para acelerar a busca
- Visualização gráfica dos grafos e caminhos
- Suporte para grafos ponderados
- Implementação do Problema do Caixeiro Viajante
- Paralelização do algoritmo de busca
- Geração automática de grafos de teste

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abrir um Pull Request

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como parte do estudo de **Fundamentos de Programação e Algoritmos Avançados (FPAA)**, demonstrando:

- Implementação de algoritmos de grafos
- Técnicas de backtracking
- Análise de complexidade computacional
- Estruturas de dados fundamentais
- Boas práticas de programação
- Classificação de problemas em classes de complexidade (P, NP, NP-Completo)

### Objetivos de Aprendizagem Atingidos:

1. **Compreensão teórica**: Entendimento das classes de complexidade e suas implicações
2. **Implementação prática**: Codificação eficiente de algoritmos de backtracking
3. **Análise matemática**: Determinação rigorosa de complexidade temporal
4. **Pensamento crítico**: Avaliação de limitações e possíveis otimizações
5. **Documentação técnica**: Elaboração de relatórios científicos completos

## 📞 Suporte

Para dúvidas, sugestões ou problemas, abra uma **issue** no repositório do projeto.

## 📄 Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.

---

**Desenvolvido com 💻 para fins educacionais e demonstração de algoritmos em teoria dos grafos.**

**Universidade**: Estudo em Fundamentos de Programação e Algoritmos Avançados  
**Tema**: Algoritmos de Grafos e Complexidade Computacional  
**Ano**: 2025
