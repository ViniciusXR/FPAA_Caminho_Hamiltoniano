# Algoritmo para Encontrar Caminho Hamiltoniano

Programa em Python que implementa o algoritmo para encontrar um Caminho Hamiltoniano em um grafo orientado ou não orientado.

## 📝 Descrição

Um **Caminho Hamiltoniano** em um grafo é um caminho que visita cada vértice exatamente uma vez. Encontrar esse caminho é um problema clássico em teoria dos grafos e está associado a problemas de alta complexidade computacional, como o Problema do Caixeiro Viajante.

Este projeto implementa uma abordagem para determinar se um Caminho Hamiltoniano existe em um grafo e, em caso afirmativo, encontrá-lo utilizando algoritmo de **backtracking**.

## 🚀 Funcionalidades

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

## 📄 Licença

Este projeto está sob a licença especificada no arquivo `LICENSE`.
