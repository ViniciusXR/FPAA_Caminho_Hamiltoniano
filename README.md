# FPAA_Caminho_Hamiltoniano
Programa desenvolvido em Python que implementa o algoritmo para encontrar um Caminho Hamiltoniano em um grafo orientado ou não orientado, utilizando a abordagem de backtracking.

## Autor: Vinicius Xavier Ramalho

## Índice

- [Implementação do Algoritmo de Caminho Hamiltoniano em Python](#implementação-do-algoritmo-de-caminho-hamiltoniano-em-python)
- [O que é o Caminho Hamiltoniano](#o-que-é-o-caminho-hamiltoniano)
- [Descrição do Projeto](#descrição-do-projeto)
  - [Algoritmo e Lógica Implementada](#algoritmo-e-lógica-implementada)
  - [Implementação das Principais Funções](#implementação-das-principais-funções)
  - [Estruturas de Dados Utilizadas](#estruturas-de-dados-utilizadas)
- [Sistema de Visualização](#sistema-de-visualização)
  - [Características da Visualização](#características-da-visualização)
  - [Exemplos de Visualizações Geradas](#exemplos-de-visualizações-geradas)
- [Como Executar o Projeto](#como-executar-o-projeto)
  - [Pré-requisitos](#pré-requisitos)
  - [Passo 1: Preparar o Ambiente](#passo-1-preparar-o-ambiente)
  - [Passo 2: Executar o Programa](#passo-2-executar-o-programa)
  - [Exemplo de Execução](#exemplo-de-execução)
- [Funcionalidades do Programa](#funcionalidades-do-programa)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Classes Principais](#classes-principais)
- [Relatório Técnico](#relatório-técnico)
  - [Análise da Complexidade Computacional](#análise-da-complexidade-computacional)
  - [Análise da Complexidade Assintótica de Tempo](#análise-da-complexidade-assintótica-de-tempo)
  - [Aplicação do Teorema Mestre](#aplicação-do-teorema-mestre)
  - [Análise dos Casos de Complexidade](#análise-dos-casos-de-complexidade)
- [Requisitos](#requisitos)
- [Características do Código](#características-do-código)
- [Possíveis Extensões](#possíveis-extensões)
- [Galeria de Visualizações](#galeria-de-visualizações)
- [Contexto Acadêmico](#contexto-acadêmico)
- [Contribuição](#contribuição)
- [Versão do Python](#versão-do-python)
- [Conclusão](#conclusão)
- [Referências](#referências)
- [Licença](#licença)

# Implementação do Algoritmo de Caminho Hamiltoniano em Python

O **Algoritmo de Caminho Hamiltoniano** é um método para encontrar um caminho que visita cada vértice de um grafo exatamente uma vez, desenvolvido utilizando a estratégia de **backtracking**. Este algoritmo explora sistematicamente todas as possibilidades, garantindo encontrar uma solução se ela existir, mas com complexidade exponencial devido à natureza NP-Completa do problema.

## O que é o Caminho Hamiltoniano

Um **Caminho Hamiltoniano** em um grafo é um caminho que visita cada vértice exatamente uma vez. Encontrar esse caminho é um problema clássico em teoria dos grafos e está associado a problemas de alta complexidade computacional, como o Problema do Caixeiro Viajante. Este problema pertence à classe **NP-Completo**, o que significa que não existe algoritmo conhecido que resolva o problema em tempo polinomial para todos os casos.

## Descrição do Projeto

O algoritmo implementado em `main.py` utiliza a abordagem recursiva do método de **backtracking** para realizar a busca eficiente do caminho hamiltoniano. A lógica do algoritmo pode ser explicada através de suas principais funções:

### Algoritmo e Lógica Implementada

O algoritmo implementado utiliza a técnica de **backtracking** (retrocesso) para explorar sistematicamente todos os possíveis caminhos no grafo. A lógica principal está dividida nas seguintes funções:

### Implementação das Principais Funções:

#### 1. **`_backtrack(vertice_atual, posicao)`**:
```python
def _backtrack(self, vertice_atual, posicao):
    # Marca o vértice atual como visitado
    self.visitados[vertice_atual] = True
    self.caminho[posicao] = vertice_atual
    
    # Se visitamos todos os vértices, encontramos um caminho hamiltoniano
    if posicao == self.grafo.num_vertices - 1:
        return True
    
    # Tenta todos os vértices adjacentes não visitados
    for proximo_vertice in self.grafo.obter_adjacentes(vertice_atual):
        if not self.visitados[proximo_vertice]:
            if self._backtrack(proximo_vertice, posicao + 1):
                return True
    
    # Backtrack: desfaz a escolha atual
    self.visitados[vertice_atual] = False
    self.caminho[posicao] = -1
    return False
```

**Função recursiva principal que implementa o algoritmo de backtracking:**
- **Linha 2-3:** Marca o vértice atual como visitado e adiciona ao caminho
- **Linha 5-7:** Verifica se todos os vértices foram visitados (condição de parada)
- **Linha 9-12:** Explora recursivamente todos os vértices adjacentes não visitados
- **Linha 14-16:** Desfaz as marcações quando não encontra solução (backtrack)

#### 2. **`encontrar_caminho(vertice_inicial=None)`**:
```python
def encontrar_caminho(self, vertice_inicial=None):
    self.caminho = [-1] * self.grafo.num_vertices
    self.visitados = [False] * self.grafo.num_vertices
    
    if vertice_inicial is not None:
        if self._backtrack(vertice_inicial, 0):
            return True, self.caminho.copy()
        else:
            return False, []
    
    # Tenta encontrar um caminho começando de cada vértice
    for vertice in range(self.grafo.num_vertices):
        self.caminho = [-1] * self.grafo.num_vertices
        self.visitados = [False] * self.grafo.num_vertices
        
        if self._backtrack(vertice, 0):
            return True, self.caminho.copy()
    
    return False, []
```

**Interface principal para buscar um caminho hamiltoniano:**
- **Linha 2-3:** Inicializa as estruturas de controle (visitados, caminho)
- **Linha 5-8:** Permite especificar um vértice inicial específico
- **Linha 10-16:** Tenta todos os vértices como ponto de partida
- **Linha 18:** Retorna se encontrou um caminho e qual é o caminho

#### 3. **`encontrar_todos_caminhos()`**:
```python
def encontrar_todos_caminhos(self):
    todos_caminhos = []
    
    def _backtrack_todos(vertice_atual, posicao, caminho_atual):
        self.visitados[vertice_atual] = True
        caminho_atual[posicao] = vertice_atual
        
        if posicao == self.grafo.num_vertices - 1:
            todos_caminhos.append(caminho_atual.copy())
        else:
            for proximo_vertice in self.grafo.obter_adjacentes(vertice_atual):
                if not self.visitados[proximo_vertice]:
                    _backtrack_todos(proximo_vertice, posicao + 1, caminho_atual)
        
        # Backtrack
        self.visitados[vertice_atual] = False
        caminho_atual[posicao] = -1
    
    for vertice_inicial in range(self.grafo.num_vertices):
        self.visitados = [False] * self.grafo.num_vertices
        caminho_temp = [-1] * self.grafo.num_vertices
        _backtrack_todos(vertice_inicial, 0, caminho_temp)
    
    return todos_caminhos
```

**Variação do algoritmo que encontra todos os caminhos hamiltonianos possíveis:**
- **Linha 4-17:** Utiliza backtracking modificado para não parar no primeiro caminho encontrado
- **Linha 19-23:** Tenta todos os vértices como ponto de partida para encontrar múltiplas soluções
- **Útil para análise completa de grafos pequenos**

### Estruturas de Dados Utilizadas:

- **Matriz de Adjacência**: Representa as conexões do grafo de forma eficiente
- **Array de Visitados**: Controla quais vértices já foram visitados no caminho atual
- **Array do Caminho**: Armazena a sequência de vértices que formam o caminho hamiltoniano

## Como Executar o Projeto

### Pré-requisitos

- **Python 3.6+** instalado no sistema
- Terminal ou prompt de comando
- **Bibliotecas opcionais** para visualização (recomendado):
  - NetworkX >= 3.0
  - Matplotlib >= 3.7.0
  - NumPy >= 1.24.0

### Passo 1: Preparar o Ambiente

1. **Clone ou baixe o repositório**:
   ```bash
   git clone https://github.com/ViniciusXR/FPAA_Caminho_Hamiltoniano.git
   cd FPAA_Caminho_Hamiltoniano
   ```

2. **(Opcional) Criar um ambiente virtual**:
   ```bash
   python -m venv .venv
   ```

3. **(Opcional) Ativar o ambiente virtual**:
   - No Windows:
   ```bash
   .venv\Scripts\activate
   ```
   - No macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

4. **Instalar dependências (opcional, mas recomendado para visualização)**:
   ```bash
   pip install -r requirements.txt
   ```

   Ou instale manualmente:
   ```bash
   pip install networkx matplotlib numpy
   ```

### Passo 2: Executar o Programa

Execute o arquivo principal:
```bash
python main.py
```

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
4. Gerar visualizações de exemplo
5. Sair

Escolha uma opção (1-5): 2

============================================================
EXECUTANDO EXEMPLOS PREDEFINIDOS
============================================================

=== Exemplo 1: Grafo Não Orientado com Caminho Hamiltoniano ===

--- Busca por Caminho Hamiltoniano: Exemplo 1 ---
✓ Caminho Hamiltoniano encontrado: 0 -> 1 -> 2 -> 3 -> 4
  Total de caminhos hamiltonianos: 14

📊 Criando visualização: Exemplo 1
✓ Visualização salva em: assets\exemplo1_grafo_com_caminho.png

=== Exemplo 2: Grafo Orientado ===

--- Busca por Caminho Hamiltoniano: Exemplo 2 ---
✓ Caminho Hamiltoniano encontrado: 0 -> 1 -> 2 -> 3

📊 Criando visualização: Exemplo 2
✓ Visualização salva em: assets\exemplo2_grafo_orientado.png
```

### 📊 Funcionalidades de Visualização

O programa inclui um sistema completo de visualização que:

- **Desenha grafos**: Mostra todos os nós e arestas com etiquetas
- **Destaca caminhos**: Realça o Caminho Hamiltoniano encontrado
- **Salva imagens**: Exporta visualizações como arquivos PNG
- **Suporta diferentes layouts**: Spring, circular, planar, etc.
- **Adiciona legendas**: Explica cores e símbolos utilizados

#### Gerando Visualizações:

**Opção 1**: Via menu interativo
```bash
python main.py
# Escolha opção 4: "Gerar visualizações de exemplo"
```

**Opção 2**: Diretamente via módulo de visualização
```bash
python view.py
```

**Opção 3**: Automática durante execução
- As visualizações são geradas automaticamente ao executar exemplos
- Imagens salvas na pasta `imagens/`

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

## Funcionalidades do Programa

- ✅ Suporte para grafos **orientados** e **não orientados**
- ✅ Busca por **um caminho hamiltoniano**
- ✅ Busca por **todos os caminhos hamiltonianos** possíveis
- ✅ Interface **interativa** com menu
- ✅ **Exemplos predefinidos** para demonstração
- ✅ Criação de **grafos personalizados**
- ✅ Geração de **grafos completos**
- ✅ Representação por **matriz de adjacência**
- ✅ **Visualização gráfica** com NetworkX e Matplotlib
- ✅ **Exportação de imagens** PNG de alta qualidade
- ✅ **Destaque automático** de Caminhos Hamiltonianos encontrados

### Opções do Menu Interativo:

- **Opção 1**: Criar grafo personalizado (permite definir vértices e arestas)
- **Opção 2**: Executar exemplos predefinidos (demonstra diferentes cenários)
- **Opção 3**: Testar grafo completo (testa grafos completos K_n)
- **Opção 4**: Gerar visualizações de exemplo (cria imagens PNG dos grafos)
- **Opção 5**: Sair do programa

## Sistema de Visualização

O projeto inclui um módulo completo de visualização (`view.py`) que utiliza **NetworkX** e **Matplotlib** para criar representações gráficas dos grafos e destacar os Caminhos Hamiltonianos.

### Características da Visualização:

#### 🎯 **Elementos Visuais:**
- **Nós destacados**: Diferentes cores para início, fim e nós intermediários
- **Arestas do caminho**: Destacadas em vermelho para visualizar o percurso
- **Numeração sequencial**: Mostra a ordem dos vértices no caminho
- **Múltiplos layouts**: Spring, circular, shell e random para diferentes perspectivas

#### 📊 **Layouts Disponíveis:**
- **Spring Layout**: Posicionamento baseado em forças físicas
- **Circular Layout**: Vértices dispostos em círculo
- **Shell Layout**: Múltiplas camadas concêntricas
- **Random Layout**: Posicionamento aleatório

#### 💾 **Exportação:**
- **Formato PNG**: Imagens de alta qualidade (300 DPI)
- **Resolução**: 1200x900 pixels para clareza
- **Salvamento automático**: Na pasta `assets/` do projeto

## Instalação

### Pré-requisitos

- **Python 3.6 ou superior**

### Instalação das Dependências

Para utilizar as funcionalidades de **visualização**, você precisa instalar as dependências:

```bash
pip install -r requirements.txt
```

**Nota**: O programa pode ser executado **sem as dependências de visualização**. Neste caso, apenas as funcionalidades básicas do algoritmo estarão disponíveis.

### Dependências Específicas

```
networkx>=3.0        # Manipulação e criação de grafos
matplotlib>=3.7.0    # Visualização e plotagem
numpy>=1.24.0        # Operações matemáticas
```

## Como Usar

### 1. Execução Básica

```bash
python main.py
```

### 2. Interface do Menu

Após executar o programa, você verá o seguinte menu:

```
=== CAMINHO HAMILTONIANO ===
1. Criar grafo personalizado
2. Executar exemplos predefinidos
3. Testar grafo completo
4. Gerar visualizações de exemplo
5. Sair

Escolha uma opção:
```

### 3. Criando um Grafo Personalizado (Opção 1)

```
Número de vértices: 4
Grafo orientado? (s/n): n
Digite as arestas (formato: a b), ou 'fim' para terminar:
0 1
1 2
2 3
3 0
fim
```

### 4. Executando Exemplos Predefinidos (Opção 2)

O programa executará automaticamente vários exemplos demonstrativos:
- Grafos com Caminho Hamiltoniano
- Grafos sem Caminho Hamiltoniano
- Grafos orientados e não orientados

### 5. Gerando Visualizações (Opção 4)

Esta opção criará **13 imagens PNG** na pasta `assets/`, mostrando:
- Diferentes tipos de grafos
- Múltiplos layouts de visualização
- Caminhos Hamiltonianos destacados

## Implementação Linha por Linha

### Estrutura Principal

O programa está organizado em duas classes principais:

```python
class Grafo:
    def __init__(self, num_vertices, orientado=False):
        """
        Inicializa um grafo com número específico de vértices.
        
        Args:
            num_vertices (int): Número de vértices do grafo
            orientado (bool): True se o grafo for orientado, False caso contrário
        """
        self.num_vertices = num_vertices
        self.orientado = orientado
        # Matriz de adjacência inicializada com zeros
        self.matriz_adj = [[0] * num_vertices for _ in range(num_vertices)]
    
    def adicionar_aresta(self, origem, destino):
        """
        Adiciona uma aresta entre dois vértices.
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
        """
        self.matriz_adj[origem][destino] = 1
        # Para grafos não orientados, adiciona aresta nos dois sentidos
        if not self.orientado:
            self.matriz_adj[destino][origem] = 1
```

#### 2. Classe `CaminhoHamiltoniano`

Esta classe implementa o algoritmo de backtracking para encontrar caminhos hamiltonianos:

```python
class CaminhoHamiltoniano:
    def __init__(self, grafo):
        """
        Inicializa o buscador de caminhos hamiltonianos.
        
        Args:
            grafo (Grafo): Instância do grafo a ser analisado
        """
        self.grafo = grafo
        self.num_vertices = grafo.num_vertices
    
    def buscar_um_caminho(self, inicio=0):
        """
        Busca um caminho hamiltoniano a partir de um vértice específico.
        
        Args:
            inicio (int): Vértice inicial do caminho
            
        Returns:
            list: Caminho hamiltoniano encontrado ou None se não existir
        """
        caminho = [-1] * self.num_vertices
        visitados = [False] * self.num_vertices
        
        # Marca o vértice inicial como visitado
        caminho[0] = inicio
        visitados[inicio] = True
        
        # Inicia a busca recursiva
        if self._buscar_recursivo(caminho, visitados, 1):
            return caminho
        return None
    
    def _buscar_recursivo(self, caminho, visitados, pos):
        """
        Método recursivo principal do backtracking.
        
        Args:
            caminho (list): Caminho atual sendo construído
            visitados (list): Lista de vértices já visitados
            pos (int): Posição atual no caminho
            
        Returns:
            bool: True se encontrou um caminho hamiltoniano, False caso contrário
        """
        # Condição de parada: visitou todos os vértices
        if pos == self.num_vertices:
            return True
        
        # Tenta cada vértice não visitado
        for v in range(self.num_vertices):
            if self._pode_adicionar(caminho[pos-1], v, visitados):
                # Adiciona vértice ao caminho
                caminho[pos] = v
                visitados[v] = True
                
                # Chamada recursiva
                if self._buscar_recursivo(caminho, visitados, pos + 1):
                    return True
                
                # Backtrack: remove vértice do caminho
                visitados[v] = False
        
        return False
    
    def _pode_adicionar(self, ultimo, novo, visitados):
        """
        Verifica se um vértice pode ser adicionado ao caminho.
        
        Args:
            ultimo (int): Último vértice do caminho atual
            novo (int): Novo vértice a ser testado
            visitados (list): Lista de vértices já visitados
            
        Returns:
            bool: True se o vértice pode ser adicionado, False caso contrário
        """
        # Verifica se existe aresta entre último e novo vértice
        if self.grafo.matriz_adj[ultimo][novo] == 0:
            return False
        
        # Verifica se o vértice já foi visitado
        if visitados[novo]:
            return False
        
        return True
```

### Algoritmo de Backtracking

O algoritmo utiliza **backtracking** para explorar sistematicamente todas as possibilidades:

#### **Passos do Algoritmo:**

1. **Inicialização**: Marca o vértice inicial como visitado
2. **Expansão**: Para cada posição no caminho, tenta todos os vértices não visitados
3. **Validação**: Verifica se existe aresta entre o último vértice e o candidato
4. **Recursão**: Chama recursivamente para a próxima posição
5. **Backtrack**: Se não encontra solução, desfaz a escolha e tenta outra

#### **Condições de Parada:**

- **Sucesso**: Quando todos os vértices foram visitados exatamente uma vez
- **Falha**: Quando não há mais vértices válidos para adicionar ao caminho

### Visualização Integrada

O sistema integra automaticamente a visualização quando as dependências estão disponíveis:

```python
# Verifica se as bibliotecas de visualização estão disponíveis
try:
    from view import VisualizadorGrafo
    VISUALIZACAO_DISPONIVEL = True
except ImportError:
    VISUALIZACAO_DISPONIVEL = False
    print("Aviso: Bibliotecas de visualização não encontradas.")
    print("Execute: pip install -r requirements.txt")

# Integração no menu principal
if VISUALIZACAO_DISPONIVEL:
    visualizador = VisualizadorGrafo()
    visualizador.visualizar_grafo(grafo_exemplo, caminho_encontrado)
```

## Relatório Técnico
### Análise de Complexidade

#### **Complexidade Temporal**

O problema do Caminho Hamiltoniano é classificado como **NP-Completo**, o que significa que não existe algoritmo conhecido que o resolva em tempo polinomial para o caso geral.

**Análise do Backtracking:**
- **Pior caso**: O(n!) onde n é o número de vértices
- **Melhor caso**: O(n) quando o caminho é encontrado na primeira tentativa
- **Caso médio**: Depende da estrutura do grafo e conectividade

**Justificativa da Complexidade O(n!):**
- No pior caso, testamos todas as permutações possíveis dos vértices
- Para n vértices, existem n! permutações possíveis
- Cada permutação requer O(n) operações para validação
- Complexidade total: O(n! × n) ≈ O(n!)

#### **Complexidade Espacial**

- **Espaço principal**: O(n) para armazenar o caminho atual
- **Espaço auxiliar**: O(n) para a lista de vértices visitados
- **Pilha de recursão**: O(n) no máximo (profundidade máxima = n)
- **Complexidade total**: O(n)

#### **Otimizações Implementadas**

1. **Verificação prévia de adjacência**: Evita explorações desnecessárias
2. **Backtracking eficiente**: Desfaz escolhas apenas quando necessário
3. **Representação por matriz**: Acesso O(1) para verificar arestas
4. **Parada antecipada**: Termina ao encontrar o primeiro caminho (modo busca única)

### Casos de Teste

#### **Teste 1: Grafo Completo K4**
```
Entrada: Grafo completo com 4 vértices
Resultado: ✅ Múltiplos caminhos hamiltonianos
Tempo: O(n) - encontrado rapidamente
```

#### **Teste 2: Grafo Linear**
```
Entrada: 0-1-2-3 (caminho linear)
Resultado: ✅ Caminho único: 0→1→2→3
Tempo: O(n) - estrutura simples
```

#### **Teste 3: Grafo Desconectado**
```
Entrada: Componentes isolados (0-1) e (2-3)
Resultado: ❌ Impossível visitar todos os vértices
Tempo: O(1) - detectado rapidamente
```

#### **Teste 4: Grafo Orientado**
```
Entrada: Grafo direcionado com ciclo
Resultado: ✅ Caminho encontrado respeitando direções
Tempo: Varia conforme conectividade
```

### Limitações e Considerações

#### **Limitações Algorítmicas**
- **Exponencial**: Impraticável para grafos com mais de ~15-20 vértices
- **Memória**: Pode esgotar pilha de recursão em grafos muito grandes
- **Determinístico**: Sempre encontra o mesmo caminho para entrada idêntica

#### **Limitações de Implementação**
- **Matriz de adjacência**: Usa O(n²) de memória sempre
- **Recursão**: Limitada pela profundidade máxima da pilha
- **Entrada manual**: Interface simples, adequada para fins didáticos

#### **Melhorias Possíveis**
- **Lista de adjacência**: Para grafos esparsos (menor uso de memória)
- **Paralelização**: Explorar múltiplos caminhos simultaneamente
- **Heurísticas**: Ordenar vértices por grau para busca mais eficiente
- **Iterativo**: Substituir recursão por pilha explícita

### Aplicações Práticas

#### **Problemas Relacionados**
- **Caixeiro Viajante**: Extensão que retorna ao vértice inicial
- **Planejamento de rotas**: Visitar todos os pontos exatamente uma vez
- **Análise de circuitos**: Verificar conectividade em componentes eletrônicos
- **Jogos de tabuleiro**: Movimentos que cobrem todas as casas

#### **Casos de Uso**
- **Educacional**: Demonstração de algoritmos de backtracking
- **Pesquisa**: Base para algoritmos mais sofisticados
- **Validação**: Teste de conectividade em pequenos grafos
- **Prototipagem**: Implementação rápida para validar conceitos

## Conclusão

Este projeto implementa uma solução completa para o problema do Caminho Hamiltoniano, combinando:

### **Características Técnicas**
- **Algoritmo robusto**: Backtracking com otimizações
- **Interface intuitiva**: Menu interativo para facilidade de uso
- **Visualização avançada**: Representação gráfica com NetworkX/Matplotlib
- **Documentação completa**: Análise detalhada de complexidade

### **Valor Educacional**
- **Demonstração prática**: De conceitos de teoria dos grafos
- **Análise de algoritmos**: Complexidade temporal e espacial detalhada
- **Implementação clara**: Código bem documentado e estruturado
- **Exemplos diversos**: Casos de teste abrangentes

### **Extensibilidade**
- **Modular**: Fácil de estender com novos algoritmos
- **Configurável**: Parâmetros ajustáveis de visualização
- **Compatível**: Funciona com e sem dependências visuais
- **Escalável**: Base sólida para implementações mais complexas

