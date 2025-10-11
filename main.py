"""
Algoritmo para encontrar um Caminho Hamiltoniano em um grafo orientado ou não orientado.

Um Caminho Hamiltoniano é um caminho que visita cada vértice exatamente uma vez.
Este programa implementa um algoritmo de backtracking para encontrar tal caminho.

Autor: Vinicius Xavier Ramalho
Data: Outubro 2025
"""

class Grafo:
    """
    Classe para representar um grafo que pode ser orientado ou não orientado.
    """
    
    def __init__(self, num_vertices, orientado=False):
        """
        Inicializa o grafo.
        
        Args:
            num_vertices (int): Número de vértices no grafo
            orientado (bool): True se o grafo for orientado, False caso contrário
        """
        self.num_vertices = num_vertices
        self.orientado = orientado
        # Matriz de adjacência para representar o grafo
        self.matriz_adj = [[False for _ in range(num_vertices)] 
                          for _ in range(num_vertices)]
        
    def adicionar_aresta(self, origem, destino):
        """
        Adiciona uma aresta ao grafo.
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
        """
        if 0 <= origem < self.num_vertices and 0 <= destino < self.num_vertices:
            self.matriz_adj[origem][destino] = True
            # Se o grafo não for orientado, adiciona a aresta inversa
            if not self.orientado:
                self.matriz_adj[destino][origem] = True
        else:
            print(f"Erro: Vértices inválidos ({origem}, {destino})")
    
    def remover_aresta(self, origem, destino):
        """
        Remove uma aresta do grafo.
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
        """
        if 0 <= origem < self.num_vertices and 0 <= destino < self.num_vertices:
            self.matriz_adj[origem][destino] = False
            if not self.orientado:
                self.matriz_adj[destino][origem] = False
    
    def tem_aresta(self, origem, destino):
        """
        Verifica se existe uma aresta entre dois vértices.
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
            
        Returns:
            bool: True se a aresta existe, False caso contrário
        """
        if 0 <= origem < self.num_vertices and 0 <= destino < self.num_vertices:
            return self.matriz_adj[origem][destino]
        return False
    
    def obter_adjacentes(self, vertice):
        """
        Obtém todos os vértices adjacentes a um dado vértice.
        
        Args:
            vertice (int): Vértice para buscar adjacentes
            
        Returns:
            list: Lista de vértices adjacentes
        """
        adjacentes = []
        for i in range(self.num_vertices):
            if self.matriz_adj[vertice][i]:
                adjacentes.append(i)
        return adjacentes
    
    def imprimir_grafo(self):
        """
        Imprime a representação do grafo.
        """
        tipo = "Orientado" if self.orientado else "Não Orientado"
        print(f"\nGrafo {tipo} com {self.num_vertices} vértices:")
        print("Matriz de Adjacência:")
        for i in range(self.num_vertices):
            print(f"  {i}: {self.matriz_adj[i]}")
        
        print("\nLista de Arestas:")
        for i in range(self.num_vertices):
            adjacentes = self.obter_adjacentes(i)
            if adjacentes:
                for j in adjacentes:
                    if self.orientado or i <= j:  # Evita duplicatas em grafos não orientados
                        simbolo = "->" if self.orientado else "--"
                        print(f"  {i} {simbolo} {j}")


class CaminhoHamiltoniano:
    """
    Classe para encontrar Caminhos Hamiltonianos em grafos.
    """
    
    def __init__(self, grafo):
        """
        Inicializa o algoritmo com um grafo.
        
        Args:
            grafo (Grafo): Instância do grafo a ser analisado
        """
        self.grafo = grafo
        self.caminho = []
        self.visitados = [False] * grafo.num_vertices
        
    def _backtrack(self, vertice_atual, posicao):
        """
        Algoritmo de backtracking para encontrar o caminho hamiltoniano.
        
        Args:
            vertice_atual (int): Vértice atual sendo visitado
            posicao (int): Posição atual no caminho
            
        Returns:
            bool: True se encontrou um caminho hamiltoniano, False caso contrário
        """
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
    
    def encontrar_caminho(self, vertice_inicial=None):
        """
        Encontra um caminho hamiltoniano no grafo.
        
        Args:
            vertice_inicial (int, optional): Vértice para iniciar a busca.
                                           Se None, tenta todos os vértices.
            
        Returns:
            tuple: (bool, list) - (encontrou_caminho, caminho)
        """
        self.caminho = [-1] * self.grafo.num_vertices
        self.visitados = [False] * self.grafo.num_vertices
        
        # Se um vértice inicial foi especificado
        if vertice_inicial is not None:
            if 0 <= vertice_inicial < self.grafo.num_vertices:
                if self._backtrack(vertice_inicial, 0):
                    return True, self.caminho.copy()
                else:
                    return False, []
            else:
                print(f"Erro: Vértice inicial inválido ({vertice_inicial})")
                return False, []
        
        # Tenta encontrar um caminho hamiltoniano começando de cada vértice
        for vertice in range(self.grafo.num_vertices):
            self.caminho = [-1] * self.grafo.num_vertices
            self.visitados = [False] * self.grafo.num_vertices
            
            if self._backtrack(vertice, 0):
                return True, self.caminho.copy()
        
        return False, []
    
    def encontrar_todos_caminhos(self):
        """
        Encontra todos os caminhos hamiltonianos possíveis no grafo.
        
        Returns:
            list: Lista de todos os caminhos hamiltonianos encontrados
        """
        todos_caminhos = []
        
        def _backtrack_todos(vertice_atual, posicao, caminho_atual):
            """Backtracking modificado para encontrar todos os caminhos."""
            self.visitados[vertice_atual] = True
            caminho_atual[posicao] = vertice_atual
            
            if posicao == self.grafo.num_vertices - 1:
                # Encontrou um caminho completo, adiciona à lista
                todos_caminhos.append(caminho_atual.copy())
            else:
                # Continua a busca
                for proximo_vertice in self.grafo.obter_adjacentes(vertice_atual):
                    if not self.visitados[proximo_vertice]:
                        _backtrack_todos(proximo_vertice, posicao + 1, caminho_atual)
            
            # Backtrack
            self.visitados[vertice_atual] = False
            caminho_atual[posicao] = -1
        
        # Tenta todos os vértices como ponto de partida
        for vertice_inicial in range(self.grafo.num_vertices):
            self.visitados = [False] * self.grafo.num_vertices
            caminho_temp = [-1] * self.grafo.num_vertices
            _backtrack_todos(vertice_inicial, 0, caminho_temp)
        
        return todos_caminhos


def criar_grafo_exemplo_1():
    """
    Cria um grafo não orientado de exemplo com caminho hamiltoniano.
    
    Returns:
        Grafo: Instância do grafo criado
    """
    print("\n=== Exemplo 1: Grafo Não Orientado com Caminho Hamiltoniano ===")
    grafo = Grafo(5, orientado=False)
    
    # Adicionando arestas para formar um grafo com caminho hamiltoniano
    arestas = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 3), (0, 4)]
    
    for origem, destino in arestas:
        grafo.adicionar_aresta(origem, destino)
    
    grafo.imprimir_grafo()
    return grafo


def criar_grafo_exemplo_2():
    """
    Cria um grafo orientado de exemplo.
    
    Returns:
        Grafo: Instância do grafo criado
    """
    print("\n=== Exemplo 2: Grafo Orientado ===")
    grafo = Grafo(4, orientado=True)
    
    # Adicionando arestas direcionadas
    arestas = [(0, 1), (1, 2), (2, 3), (0, 3)]
    
    for origem, destino in arestas:
        grafo.adicionar_aresta(origem, destino)
    
    grafo.imprimir_grafo()
    return grafo


def criar_grafo_exemplo_3():
    """
    Cria um grafo sem caminho hamiltoniano.
    
    Returns:
        Grafo: Instância do grafo criado
    """
    print("\n=== Exemplo 3: Grafo sem Caminho Hamiltoniano ===")
    grafo = Grafo(4, orientado=False)
    
    # Grafo desconectado - não pode ter caminho hamiltoniano
    arestas = [(0, 1), (2, 3)]
    
    for origem, destino in arestas:
        grafo.adicionar_aresta(origem, destino)
    
    grafo.imprimir_grafo()
    return grafo


def criar_grafo_completo(n):
    """
    Cria um grafo completo com n vértices.
    
    Args:
        n (int): Número de vértices
        
    Returns:
        Grafo: Instância do grafo completo criado
    """
    print(f"\n=== Grafo Completo com {n} vértices ===")
    grafo = Grafo(n, orientado=False)
    
    # Conecta todos os vértices entre si
    for i in range(n):
        for j in range(i + 1, n):
            grafo.adicionar_aresta(i, j)
    
    grafo.imprimir_grafo()
    return grafo


def tentar_visualizacao(grafo, caminho, nome_exemplo):
    """
    Tenta criar uma visualização do grafo usando o módulo view.py.
    
    Args:
        grafo (Grafo): Instância do grafo
        caminho (List[int] ou None): Caminho hamiltoniano encontrado
        nome_exemplo (str): Nome do exemplo para o arquivo
    """
    try:
        from view import VisualizadorGrafo
        
        print(f"\n📊 Criando visualização: {nome_exemplo}")
        
        # Cria visualizador
        visualizador = VisualizadorGrafo(grafo)
        
        # Gera nome do arquivo baseado no exemplo
        nome_arquivo = nome_exemplo.lower().replace(" ", "_").replace(":", "")
        
        # Cria visualização
        arquivo_salvo = visualizador.visualizar_grafo_completo(
            caminho=caminho,
            titulo=nome_exemplo,
            salvar=True,
            nome_arquivo=nome_arquivo,
            mostrar=False  # Não mostra para não interromper execução em lote
        )
        
        if arquivo_salvo:
            print(f"✓ Visualização salva em: {arquivo_salvo}")
        else:
            print("✗ Erro ao salvar visualização")
            
    except ImportError:
        print("📊 Visualização não disponível. Para ativar, instale as dependências:")
        print("   pip install -r requirements.txt")
    except Exception as e:
        print(f"📊 Erro na visualização: {e}")


def executar_busca_caminho(grafo, nome_exemplo, mostrar_visualizacao=True):
    """
    Executa a busca por caminho hamiltoniano em um grafo.
    
    Args:
        grafo (Grafo): Grafo para analisar
        nome_exemplo (str): Nome do exemplo para exibição
        mostrar_visualizacao (bool): Se deve tentar mostrar visualização
    """
    print(f"\n--- Busca por Caminho Hamiltoniano: {nome_exemplo} ---")
    
    algoritmo = CaminhoHamiltoniano(grafo)
    
    # Busca um caminho hamiltoniano
    encontrou, caminho = algoritmo.encontrar_caminho()
    
    if encontrou:
        print(f"✓ Caminho Hamiltoniano encontrado: {' -> '.join(map(str, caminho))}")
        
        # Verifica se queremos encontrar todos os caminhos (apenas para grafos pequenos)
        if grafo.num_vertices <= 5:
            todos_caminhos = algoritmo.encontrar_todos_caminhos()
            if len(todos_caminhos) > 1:
                print(f"  Total de caminhos hamiltonianos: {len(todos_caminhos)}")
                print("  Outros caminhos encontrados:")
                for i, caminho_alt in enumerate(todos_caminhos[1:6], 1):  # Mostra até 5 alternativos
                    print(f"    {i}: {' -> '.join(map(str, caminho_alt))}")
                if len(todos_caminhos) > 6:
                    print(f"    ... e mais {len(todos_caminhos) - 6} caminhos")
        
    else:
        print("✗ Nenhum Caminho Hamiltoniano encontrado")
    
    # Tentativa de visualização (se bibliotecas estiverem disponíveis)
    if mostrar_visualizacao and grafo.num_vertices <= 10:  # Limita visualização para grafos pequenos
        tentar_visualizacao(grafo, caminho if encontrou else None, nome_exemplo)


def menu_interativo():
    """
    Executa um menu interativo para o usuário criar e testar grafos.
    """
    print("\n" + "="*60)
    print("MENU INTERATIVO - CAMINHO HAMILTONIANO")
    print("="*60)
    
    while True:
        print("\nOpções:")
        print("1. Criar grafo personalizado")
        print("2. Executar exemplos predefinidos")
        print("3. Testar grafo completo")
        print("4. Gerar visualizações de exemplo")
        print("5. Sair")
        
        try:
            opcao = input("\nEscolha uma opção (1-5): ").strip()
            
            if opcao == '1':
                criar_grafo_personalizado()
            elif opcao == '2':
                executar_exemplos()
            elif opcao == '3':
                testar_grafo_completo()
            elif opcao == '4':
                gerar_visualizacoes_exemplo()
            elif opcao == '5':
                print("Encerrando programa...")
                break
            else:
                print("Opção inválida! Tente novamente.")
                
        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro: {e}")


def criar_grafo_personalizado():
    """
    Permite ao usuário criar um grafo personalizado.
    """
    try:
        print("\n--- Criação de Grafo Personalizado ---")
        
        num_vertices = int(input("Número de vértices: "))
        if num_vertices <= 0:
            print("Número de vértices deve ser positivo!")
            return
            
        orientado_input = input("Grafo orientado? (s/n): ").strip().lower()
        orientado = orientado_input in ['s', 'sim', 'y', 'yes']
        
        grafo = Grafo(num_vertices, orientado)
        
        print(f"\nCriando grafo {'orientado' if orientado else 'não orientado'} com {num_vertices} vértices")
        print("Vértices numerados de 0 a", num_vertices - 1)
        print("Digite as arestas (formato: origem destino)")
        print("Digite 'fim' para terminar")
        
        while True:
            entrada = input("Aresta (origem destino): ").strip()
            if entrada.lower() == 'fim':
                break
                
            try:
                origem, destino = map(int, entrada.split())
                grafo.adicionar_aresta(origem, destino)
                print(f"Aresta {origem} -> {destino} adicionada")
            except ValueError:
                print("Formato inválido! Use: origem destino")
            except Exception as e:
                print(f"Erro ao adicionar aresta: {e}")
        
        grafo.imprimir_grafo()
        executar_busca_caminho(grafo, "Grafo Personalizado")
        
    except ValueError:
        print("Entrada inválida! Use números inteiros.")
    except Exception as e:
        print(f"Erro: {e}")


def testar_grafo_completo():
    """
    Testa um grafo completo com número de vértices especificado pelo usuário.
    """
    try:
        n = int(input("\nNúmero de vértices para o grafo completo: "))
        if n <= 0:
            print("Número de vértices deve ser positivo!")
            return
        if n > 8:
            print("Aviso: Grafos completos com muitos vértices podem demorar para processar!")
            
        grafo = criar_grafo_completo(n)
        executar_busca_caminho(grafo, f"Grafo Completo K{n}")
        
    except ValueError:
        print("Entrada inválida! Use um número inteiro.")


def executar_exemplos():
    """
    Executa todos os exemplos predefinidos.
    """
    print("\n" + "="*60)
    print("EXECUTANDO EXEMPLOS PREDEFINIDOS")
    print("="*60)
    
    # Exemplo 1: Grafo não orientado com caminho hamiltoniano
    grafo1 = criar_grafo_exemplo_1()
    executar_busca_caminho(grafo1, "Exemplo 1")
    
    # Exemplo 2: Grafo orientado
    grafo2 = criar_grafo_exemplo_2()
    executar_busca_caminho(grafo2, "Exemplo 2")
    
    # Exemplo 3: Grafo sem caminho hamiltoniano
    grafo3 = criar_grafo_exemplo_3()
    executar_busca_caminho(grafo3, "Exemplo 3")
    
    # Exemplo 4: Grafo completo pequeno
    grafo4 = criar_grafo_completo(4)
    executar_busca_caminho(grafo4, "Grafo Completo K4")


def gerar_visualizacoes_exemplo():
    """
    Gera visualizações de todos os exemplos usando o módulo view.py.
    """
    try:
        from view import criar_visualizacoes_exemplo
        
        print("\n" + "="*60)
        print("GERANDO VISUALIZAÇÕES DE EXEMPLO")
        print("="*60)
        print("\nEsta função criará visualizações PNG de vários exemplos de grafos.")
        print("As imagens serão salvas na pasta 'assets/'.")
        
        confirmacao = input("\nDeseja continuar? (s/n): ").strip().lower()
        if confirmacao in ['s', 'sim', 'y', 'yes']:
            criar_visualizacoes_exemplo()
        else:
            print("Operação cancelada.")
            
    except ImportError:
        print("\n❌ Módulo de visualização não disponível.")
        print("Para usar esta funcionalidade, instale as dependências:")
        print("   pip install -r requirements.txt")
    except Exception as e:
        print(f"\n❌ Erro ao gerar visualizações: {e}")


def main():
    """
    Função principal do programa.
    """
    print("="*60)
    print("ALGORITMO PARA ENCONTRAR CAMINHO HAMILTONIANO")
    print("="*60)
    print("\nUm Caminho Hamiltoniano é um caminho em um grafo que visita")
    print("cada vértice exatamente uma vez.")
    print("\nEste programa utiliza algoritmo de backtracking para encontrar")
    print("caminhos hamiltonianos em grafos orientados e não orientados.")
    
    try:
        menu_interativo()
    except Exception as e:
        print(f"Erro fatal: {e}")
    finally:
        print("\nObrigado por usar o programa!")


if __name__ == "__main__":
    main()