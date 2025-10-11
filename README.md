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
- **Bibliotecas opcionais** para visualização (recomendado):
  - NetworkX >= 3.0
  - Matplotlib >= 3.7.0
  - NumPy >= 1.24.0

### Instalação das Dependências

**Para funcionalidade básica** (apenas algoritmo):
```bash
# Nenhuma instalação necessária - usa apenas bibliotecas padrão do Python
python main.py
```

**Para funcionalidade completa** (com visualização):
```bash
# Instala as dependências de visualização
pip install -r requirements.txt
```

Ou instale manualmente:
```bash
pip install networkx matplotlib numpy
```

### Instruções para Execução Local

1. **Clone ou baixe o repositório**:
   ```bash
   git clone https://github.com/ViniciusXR/FPAA_Caminho_Hamiltoniano.git
   cd FPAA_Caminho_Hamiltoniano
   ```

2. **Instale as dependências (opcional, mas recomendado)**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o programa principal**:
   ```bash
   python main.py
   ```

4. **Navegue pelo menu interativo**:
   - O programa apresentará um menu com 5 opções
   - Escolha a opção desejada digitando o número correspondente
   - Siga as instruções na tela para cada funcionalidade

### Opções Disponíveis:

- **Opção 1**: Criar grafo personalizado (permite definir vértices e arestas)
- **Opção 2**: Executar exemplos predefinidos (demonstra diferentes cenários)
- **Opção 3**: Testar grafo completo (testa grafos completos K_n)
- **Opção 4**: Gerar visualizações de exemplo (cria imagens PNG dos grafos)
- **Opção 5**: Sair do programa

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
- Imagens salvas na pasta `assets/`

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

Escolha uma opção (1-5): 4

============================================================
GERANDO VISUALIZAÇÕES DE EXEMPLO
============================================================

Deseja continuar? (s/n): s

1. Criando exemplo: Grafo com Caminho Hamiltoniano
✓ Visualização salva em: assets\exemplo1_grafo_com_caminho.png

2. Criando exemplo: Grafo Orientado  
✓ Visualização salva em: assets\exemplo2_grafo_orientado.png
```
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
- ✅ **Visualização gráfica** com NetworkX e Matplotlib
- ✅ **Exportação de imagens** PNG de alta qualidade
- ✅ **Destaque automático** de Caminhos Hamiltonianos encontrados

## 🎨 Sistema de Visualização

O projeto inclui um módulo completo de visualização (`view.py`) que utiliza **NetworkX** e **Matplotlib** para criar representações gráficas dos grafos e destacar os Caminhos Hamiltonianos.

### Características da Visualização:

#### 🎯 **Elementos Visuais:**
- **Nós (Vértices)**: Círculos coloridos com números identificadores
- **Arestas**: Linhas conectando os vértices
- **Direcionamento**: Setas para grafos orientados
- **Legenda**: Explicação dos elementos visuais

#### 🌈 **Sistema de Cores:**
- **Nós normais**: Azul claro (`#87CEEB`)
- **Início do caminho**: Verde (`#32CD32`)
- **Fim do caminho**: Vermelho (`#FF6347`)
- **Nós intermediários**: Dourado (`#FFD700`)
- **Arestas normais**: Cinza (`#696969`)
- **Caminho Hamiltoniano**: Laranja-vermelho (`#FF4500`)

#### 📐 **Layouts Disponíveis:**
- **Spring**: Distribuição baseada em forças físicas (padrão)
- **Circular**: Vértices dispostos em círculo
- **Planar**: Layout planar quando possível
- **Shell**: Múltiplas camadas concêntricas
- **Kamada-Kawai**: Algoritmo de posicionamento avançado

### 📊 Exemplos de Visualizações Geradas:

#### **Exemplo 1: Grafo Não Orientado com Caminho Hamiltoniano**
- **Arquivo**: `assets/exemplo1_grafo_com_caminho.png`
- **Descrição**: Grafo de 5 vértices com múltiplos caminhos hamiltonianos
- **Caminho destacado**: 0 → 1 → 2 → 3 → 4
- **Layout**: Spring

#### **Exemplo 2: Grafo Orientado**
- **Arquivo**: `assets/exemplo2_grafo_orientado.png`
- **Descrição**: Grafo direcionado de 4 vértices
- **Caminho destacado**: 0 → 1 → 2 → 3
- **Layout**: Circular

#### **Exemplo 3: Grafo sem Caminho Hamiltoniano**
- **Arquivo**: `assets/exemplo3_grafo_sem_caminho.png`
- **Descrição**: Grafo desconectado (componentes isolados)
- **Status**: Nenhum caminho hamiltoniano possível
- **Layout**: Spring

#### **Exemplo 4: Grafo Completo K4**
- **Arquivo**: `assets/exemplo4_grafo_completo_k4.png`
- **Descrição**: Grafo completo com 4 vértices
- **Caminho destacado**: 0 → 1 → 2 → 3
- **Layout**: Circular

### 🔧 Configurações Visuais:

```python
# Configurações padrão do visualizador
config = {
    'node_size': 800,           # Tamanho dos nós
    'node_color': '#87CEEB',    # Cor dos nós
    'edge_width': 2,            # Espessura das arestas
    'path_width': 4,            # Espessura do caminho
    'font_size': 12,            # Tamanho da fonte
    'figure_size': (12, 8),     # Tamanho da figura
    'dpi': 300                  # Resolução da imagem
}
```

## 🏗️ Estrutura do Projeto

```
FPAA_Caminho_Hamiltoniano/
├── main.py                      # Programa principal
├── view.py                      # Módulo de visualização
├── exemplo_visualizacao.py      # Exemplo de uso da visualização
├── requirements.txt             # Dependências para visualização
├── README.md                   # Documentação completa
├── LICENSE                     # Licença do projeto
└── assets/                     # Pasta com visualizações geradas
    ├── exemplo1_grafo_com_caminho.png
    ├── exemplo2_grafo_orientado.png
    ├── exemplo3_grafo_sem_caminho.png
    ├── exemplo4_grafo_completo_k4.png
    └── exemplo_personalizado.png
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

### `VisualizadorGrafo` (view.py)
Classe para visualização gráfica de grafos e caminhos hamiltonianos.

**Métodos principais:**
- `criar_networkx_graph()` - Converte Grafo para NetworkX
- `calcular_layout(layout_type)` - Define disposição dos vértices
- `desenhar_grafo_base()` - Desenha estrutura básica do grafo
- `destacar_caminho_hamiltoniano(caminho)` - Realça o caminho encontrado
- `visualizar_grafo_completo()` - Função principal de visualização
- `salvar_imagem(nome_arquivo)` - Exporta visualização como PNG

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

### Requisitos Básicos (Algoritmo apenas):
- **Python 3.6+**
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão)

### Requisitos Completos (Com visualização):
- **Python 3.6+**
- **NetworkX** >= 3.0 (manipulação de grafos)
- **Matplotlib** >= 3.7.0 (visualização e exportação)
- **NumPy** >= 1.24.0 (cálculos matemáticos)

### Instalação das Dependências:

```bash
# Opção 1: Via requirements.txt (recomendado)
pip install -r requirements.txt

# Opção 2: Instalação manual
pip install networkx matplotlib numpy
```

## 🎨 Características do Código

- **Documentação completa** com docstrings
- **Tratamento de erros** robusto
- **Interface amigável** com menu interativo
- **Código modular** e reutilizável
- **Exemplos práticos** incluídos
- **Suporte a diferentes tipos** de grafo

## 📄 Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.


---

## 🖼️ Galeria de Visualizações

O repositório inclui exemplos de visualizações geradas automaticamente na pasta `assets/`:

### 📊 Imagens Disponíveis:
- **`exemplo1_grafo_com_caminho.png`** - Grafo não orientado com múltiplos caminhos
- **`exemplo2_grafo_orientado.png`** - Grafo direcionado com caminho único  
- **`exemplo3_grafo_sem_caminho.png`** - Grafo desconectado sem solução
- **`exemplo4_grafo_completo_k4.png`** - Grafo completo K4

### 🎨 Características das Visualizações:
- **Alta resolução** (300 DPI) para uso acadêmico
- **Cores distintivas** para diferentes elementos
- **Legendas explicativas** incluídas
- **Informações textuais** sobre o grafo
- **Layouts otimizados** para clareza visual

### 📋 Como Reproduzir:
```bash
# Gerar todas as visualizações
python view.py

# Ou via menu interativo
python main.py
# Escolha opção 4: "Gerar visualizações de exemplo"
```

---

