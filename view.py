"""
Módulo de visualização para Grafos e Caminhos Hamiltonianos.

Este módulo fornece funcionalidades para visualizar grafos usando NetworkX e Matplotlib,
com destaque especial para Caminhos Hamiltonianos encontrados.

Dependências:
- networkx: Para criação e manipulação de grafos
- matplotlib: Para visualização e geração de imagens
- numpy: Para cálculos matemáticos auxiliares

Autor: Desenvolvido para demonstração acadêmica
Data: Outubro 2025
"""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
from typing import List, Tuple, Optional, Dict, Any


class VisualizadorGrafo:
    """
    Classe para visualização de grafos e caminhos hamiltonianos.
    """
    
    def __init__(self, grafo_obj=None):
        """
        Inicializa o visualizador.
        
        Args:
            grafo_obj: Instância da classe Grafo do main.py
        """
        self.grafo_obj = grafo_obj
        self.nx_graph = None
        self.pos = None
        self.fig = None
        self.ax = None
        
        # Configurações visuais
        self.config = {
            'node_size': 800,
            'node_color': '#87CEEB',  # SkyBlue
            'node_border_color': '#4682B4',  # SteelBlue
            'edge_color': '#696969',  # DimGray
            'edge_width': 2,
            'path_color': '#FF4500',  # OrangeRed
            'path_width': 4,
            'font_size': 12,
            'font_weight': 'bold',
            'font_color': '#000000',
            'figure_size': (12, 8),
            'dpi': 300
        }
    
    def criar_networkx_graph(self, grafo_obj=None):
        """
        Converte a instância do Grafo para um NetworkX graph.
        
        Args:
            grafo_obj: Instância da classe Grafo (opcional)
            
        Returns:
            networkx.Graph ou networkx.DiGraph
        """
        if grafo_obj is None:
            grafo_obj = self.grafo_obj
            
        if grafo_obj is None:
            raise ValueError("Nenhum grafo fornecido para conversão")
        
        # Cria grafo direcionado ou não direcionado
        if grafo_obj.orientado:
            self.nx_graph = nx.DiGraph()
        else:
            self.nx_graph = nx.Graph()
        
        # Adiciona vértices
        for i in range(grafo_obj.num_vertices):
            self.nx_graph.add_node(i)
        
        # Adiciona arestas
        for i in range(grafo_obj.num_vertices):
            for j in range(grafo_obj.num_vertices):
                if grafo_obj.matriz_adj[i][j]:
                    if not grafo_obj.orientado and i > j:
                        continue  # Evita arestas duplicadas em grafos não orientados
                    self.nx_graph.add_edge(i, j)
        
        return self.nx_graph
    
    def calcular_layout(self, layout_type='spring', **kwargs):
        """
        Calcula o layout dos nós para visualização.
        
        Args:
            layout_type (str): Tipo de layout ('spring', 'circular', 'planar', 'shell')
            **kwargs: Argumentos adicionais para o layout
            
        Returns:
            dict: Posições dos nós
        """
        if self.nx_graph is None:
            raise ValueError("Graph NetworkX não foi criado")
        
        layouts = {
            'spring': nx.spring_layout,
            'circular': nx.circular_layout,
            'planar': nx.planar_layout,
            'shell': nx.shell_layout,
            'kamada_kawai': nx.kamada_kawai_layout,
            'spectral': nx.spectral_layout
        }
        
        if layout_type not in layouts:
            layout_type = 'spring'
        
        try:
            layout_func = layouts[layout_type]
            
            # Configurações específicas para diferentes layouts
            if layout_type == 'spring':
                kwargs.setdefault('k', 2)
                kwargs.setdefault('iterations', 50)
                kwargs.setdefault('seed', 42)
            elif layout_type == 'kamada_kawai':
                kwargs.setdefault('scale', 2)
            
            self.pos = layout_func(self.nx_graph, **kwargs)
            
        except Exception as e:
            print(f"Erro ao calcular layout {layout_type}: {e}")
            print("Usando layout spring como fallback")
            self.pos = nx.spring_layout(self.nx_graph, k=2, iterations=50, seed=42)
        
        return self.pos
    
    def configurar_figura(self, titulo="Grafo", tamanho=(12, 8)):
        """
        Configura a figura matplotlib.
        
        Args:
            titulo (str): Título da figura
            tamanho (tuple): Tamanho da figura (largura, altura)
        """
        plt.style.use('default')
        self.fig, self.ax = plt.subplots(figsize=tamanho, dpi=self.config['dpi'])
        self.ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        
        # Adiciona grid sutil
        self.ax.grid(True, alpha=0.1)
    
    def desenhar_grafo_base(self):
        """
        Desenha o grafo base (nós e arestas originais).
        """
        if self.nx_graph is None or self.pos is None:
            raise ValueError("Graph e posições devem ser configurados primeiro")
        
        # Desenha arestas
        if self.grafo_obj.orientado:
            nx.draw_networkx_edges(
                self.nx_graph, self.pos,
                edge_color=self.config['edge_color'],
                width=self.config['edge_width'],
                alpha=0.7,
                arrows=True,
                arrowsize=20,
                arrowstyle='->',
                ax=self.ax
            )
        else:
            nx.draw_networkx_edges(
                self.nx_graph, self.pos,
                edge_color=self.config['edge_color'],
                width=self.config['edge_width'],
                alpha=0.7,
                ax=self.ax
            )
        
        # Desenha nós
        nx.draw_networkx_nodes(
            self.nx_graph, self.pos,
            node_color=self.config['node_color'],
            node_size=self.config['node_size'],
            edgecolors=self.config['node_border_color'],
            linewidths=2,
            ax=self.ax
        )
        
        # Adiciona rótulos dos nós
        nx.draw_networkx_labels(
            self.nx_graph, self.pos,
            font_size=self.config['font_size'],
            font_weight=self.config['font_weight'],
            font_color=self.config['font_color'],
            ax=self.ax
        )
    
    def destacar_caminho_hamiltoniano(self, caminho: List[int]):
        """
        Destaca o caminho hamiltoniano no grafo.
        
        Args:
            caminho (List[int]): Lista de vértices do caminho hamiltoniano
        """
        if not caminho or len(caminho) < 2:
            return
        
        # Cria lista de arestas do caminho
        arestas_caminho = [(caminho[i], caminho[i + 1]) for i in range(len(caminho) - 1)]
        
        # Desenha arestas do caminho com destaque
        if self.grafo_obj.orientado:
            nx.draw_networkx_edges(
                self.nx_graph, self.pos,
                edgelist=arestas_caminho,
                edge_color=self.config['path_color'],
                width=self.config['path_width'],
                alpha=0.9,
                arrows=True,
                arrowsize=25,
                arrowstyle='->',
                ax=self.ax
            )
        else:
            nx.draw_networkx_edges(
                self.nx_graph, self.pos,
                edgelist=arestas_caminho,
                edge_color=self.config['path_color'],
                width=self.config['path_width'],
                alpha=0.9,
                ax=self.ax
            )
        
        # Destaca nós do caminho
        cores_nos = []
        for node in self.nx_graph.nodes():
            if node in caminho:
                if node == caminho[0]:
                    cores_nos.append('#32CD32')  # Verde para início
                elif node == caminho[-1]:
                    cores_nos.append('#FF6347')  # Vermelho para fim
                else:
                    cores_nos.append('#FFD700')  # Dourado para intermediários
            else:
                cores_nos.append(self.config['node_color'])
        
        nx.draw_networkx_nodes(
            self.nx_graph, self.pos,
            node_color=cores_nos,
            node_size=self.config['node_size'],
            edgecolors=self.config['node_border_color'],
            linewidths=2,
            ax=self.ax
        )
    
    def adicionar_legenda(self, caminho_encontrado: bool = False):
        """
        Adiciona legenda explicativa à visualização.
        
        Args:
            caminho_encontrado (bool): Se um caminho hamiltoniano foi encontrado
        """
        elementos_legenda = []
        labels_legenda = []
        
        # Nó normal
        elementos_legenda.append(patches.Circle((0, 0), 0.1, 
                                               facecolor=self.config['node_color'],
                                               edgecolor=self.config['node_border_color']))
        labels_legenda.append('Vértice')
        
        # Aresta normal
        elementos_legenda.append(patches.Rectangle((0, 0), 0.2, 0.02,
                                                 facecolor=self.config['edge_color']))
        labels_legenda.append('Aresta')
        
        if caminho_encontrado:
            # Nó inicial
            elementos_legenda.append(patches.Circle((0, 0), 0.1,
                                                   facecolor='#32CD32',
                                                   edgecolor=self.config['node_border_color']))
            labels_legenda.append('Início do Caminho')
            
            # Nó final
            elementos_legenda.append(patches.Circle((0, 0), 0.1,
                                                   facecolor='#FF6347',
                                                   edgecolor=self.config['node_border_color']))
            labels_legenda.append('Fim do Caminho')
            
            # Caminho hamiltoniano
            elementos_legenda.append(patches.Rectangle((0, 0), 0.2, 0.04,
                                                     facecolor=self.config['path_color']))
            labels_legenda.append('Caminho Hamiltoniano')
        
        self.ax.legend(elementos_legenda, labels_legenda,
                      loc='upper left', bbox_to_anchor=(1.02, 1),
                      frameon=True, fancybox=True, shadow=True)
    
    def adicionar_informacoes(self, caminho: Optional[List[int]] = None):
        """
        Adiciona informações textuais sobre o grafo.
        
        Args:
            caminho (Optional[List[int]]): Caminho hamiltoniano se encontrado
        """
        info_text = []
        
        # Informações básicas do grafo
        info_text.append(f"Vértices: {self.grafo_obj.num_vertices}")
        info_text.append(f"Arestas: {len(self.nx_graph.edges())}")
        info_text.append(f"Tipo: {'Orientado' if self.grafo_obj.orientado else 'Não Orientado'}")
        
        if caminho:
            info_text.append(f"Caminho Hamiltoniano: {' → '.join(map(str, caminho))}")
            info_text.append(f"Comprimento: {len(caminho)} vértices")
        else:
            info_text.append("Caminho Hamiltoniano: Não encontrado")
        
        # Posiciona o texto na parte inferior
        info_str = '\n'.join(info_text)
        self.ax.text(0.02, 0.02, info_str,
                    transform=self.ax.transAxes,
                    fontsize=10,
                    verticalalignment='bottom',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.8))
    
    def salvar_imagem(self, nome_arquivo: str, pasta_destino: str = 'imagens'):
        """
        Salva a visualização como imagem PNG.
        
        Args:
            nome_arquivo (str): Nome do arquivo (sem extensão)
            pasta_destino (str): Pasta de destino
        """
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        
        caminho_completo = os.path.join(pasta_destino, f"{nome_arquivo}.png")
        
        plt.tight_layout()
        plt.savefig(caminho_completo, 
                   dpi=self.config['dpi'],
                   bbox_inches='tight',
                   facecolor='white',
                   edgecolor='none')
        
        print(f"Imagem salva em: {caminho_completo}")
        return caminho_completo
    
    def visualizar_grafo_completo(self, caminho: Optional[List[int]] = None,
                                  titulo: str = "Grafo e Caminho Hamiltoniano",
                                  layout: str = 'spring',
                                  salvar: bool = True,
                                  nome_arquivo: str = None,
                                  mostrar: bool = True):
        """
        Função principal para visualização completa do grafo.
        
        Args:
            caminho (Optional[List[int]]): Caminho hamiltoniano para destacar
            titulo (str): Título da visualização
            layout (str): Tipo de layout
            salvar (bool): Se deve salvar a imagem
            nome_arquivo (str): Nome do arquivo para salvar
            mostrar (bool): Se deve mostrar a imagem
            
        Returns:
            str: Caminho do arquivo salvo (se salvar=True)
        """
        try:
            # 1. Criar NetworkX graph
            self.criar_networkx_graph()
            
            # 2. Calcular layout
            self.calcular_layout(layout)
            
            # 3. Configurar figura
            self.configurar_figura(titulo)
            
            # 4. Desenhar grafo base
            self.desenhar_grafo_base()
            
            # 5. Destacar caminho (se fornecido)
            if caminho:
                self.destacar_caminho_hamiltoniano(caminho)
            
            # 6. Adicionar legenda
            self.adicionar_legenda(caminho_encontrado=bool(caminho))
            
            # 7. Adicionar informações
            self.adicionar_informacoes(caminho)
            
            # 8. Salvar imagem
            caminho_arquivo = None
            if salvar:
                if nome_arquivo is None:
                    if caminho:
                        nome_arquivo = f"grafo_com_caminho_hamiltoniano"
                    else:
                        nome_arquivo = f"grafo_sem_caminho_hamiltoniano"
                
                caminho_arquivo = self.salvar_imagem(nome_arquivo)
            
            # 9. Mostrar imagem
            if mostrar:
                plt.show()
            else:
                plt.close()
            
            return caminho_arquivo
            
        except Exception as e:
            print(f"Erro na visualização: {e}")
            return None


def criar_visualizacoes_exemplo():
    """
    Cria visualizações de exemplo para demonstração.
    """
    print("Criando visualizações de exemplo...")
    
    # Importa as classes do main.py
    try:
        from main import Grafo, CaminhoHamiltoniano
    except ImportError:
        print("Erro: Não foi possível importar classes do main.py")
        return
    
    exemplos = []
    
    # Exemplo 1: Grafo com caminho hamiltoniano
    print("\n1. Criando exemplo: Grafo com Caminho Hamiltoniano")
    grafo1 = Grafo(5, orientado=False)
    arestas1 = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 3), (0, 4)]
    for origem, destino in arestas1:
        grafo1.adicionar_aresta(origem, destino)
    
    algoritmo1 = CaminhoHamiltoniano(grafo1)
    encontrou1, caminho1 = algoritmo1.encontrar_caminho()
    
    visualizador1 = VisualizadorGrafo(grafo1)
    arquivo1 = visualizador1.visualizar_grafo_completo(
        caminho=caminho1 if encontrou1 else None,
        titulo="Exemplo 1: Grafo Não Orientado com Caminho Hamiltoniano",
        nome_arquivo="exemplo1_grafo_com_caminho",
        mostrar=False
    )
    exemplos.append(("Exemplo 1", arquivo1, encontrou1, caminho1))
    
    # Exemplo 2: Grafo orientado
    print("\n2. Criando exemplo: Grafo Orientado")
    grafo2 = Grafo(4, orientado=True)
    arestas2 = [(0, 1), (1, 2), (2, 3), (0, 3)]
    for origem, destino in arestas2:
        grafo2.adicionar_aresta(origem, destino)
    
    algoritmo2 = CaminhoHamiltoniano(grafo2)
    encontrou2, caminho2 = algoritmo2.encontrar_caminho()
    
    visualizador2 = VisualizadorGrafo(grafo2)
    arquivo2 = visualizador2.visualizar_grafo_completo(
        caminho=caminho2 if encontrou2 else None,
        titulo="Exemplo 2: Grafo Orientado",
        nome_arquivo="exemplo2_grafo_orientado",
        layout='circular',
        mostrar=False
    )
    exemplos.append(("Exemplo 2", arquivo2, encontrou2, caminho2))
    
    # Exemplo 3: Grafo sem caminho hamiltoniano
    print("\n3. Criando exemplo: Grafo sem Caminho Hamiltoniano")
    grafo3 = Grafo(4, orientado=False)
    arestas3 = [(0, 1), (2, 3)]  # Grafo desconectado
    for origem, destino in arestas3:
        grafo3.adicionar_aresta(origem, destino)
    
    algoritmo3 = CaminhoHamiltoniano(grafo3)
    encontrou3, caminho3 = algoritmo3.encontrar_caminho()
    
    visualizador3 = VisualizadorGrafo(grafo3)
    arquivo3 = visualizador3.visualizar_grafo_completo(
        caminho=caminho3 if encontrou3 else None,
        titulo="Exemplo 3: Grafo Desconectado (sem Caminho Hamiltoniano)",
        nome_arquivo="exemplo3_grafo_sem_caminho",
        layout='spring',
        mostrar=False
    )
    exemplos.append(("Exemplo 3", arquivo3, encontrou3, caminho3))
    
    # Exemplo 4: Grafo completo pequeno
    print("\n4. Criando exemplo: Grafo Completo K4")
    grafo4 = Grafo(4, orientado=False)
    for i in range(4):
        for j in range(i + 1, 4):
            grafo4.adicionar_aresta(i, j)
    
    algoritmo4 = CaminhoHamiltoniano(grafo4)
    encontrou4, caminho4 = algoritmo4.encontrar_caminho()
    
    visualizador4 = VisualizadorGrafo(grafo4)
    arquivo4 = visualizador4.visualizar_grafo_completo(
        caminho=caminho4 if encontrou4 else None,
        titulo="Exemplo 4: Grafo Completo K4",
        nome_arquivo="exemplo4_grafo_completo_k4",
        layout='circular',
        mostrar=False
    )
    exemplos.append(("Exemplo 4", arquivo4, encontrou4, caminho4))
    
    # Resumo dos exemplos criados
    print("\n" + "="*60)
    print("RESUMO DAS VISUALIZAÇÕES CRIADAS")
    print("="*60)
    
    for nome, arquivo, encontrou, caminho in exemplos:
        status = "✓ Caminho encontrado" if encontrou else "✗ Sem caminho"
        caminho_str = f": {' → '.join(map(str, caminho))}" if encontrou and caminho else ""
        print(f"{nome}")
        print(f"  Arquivo: {arquivo}")
        print(f"  Status: {status}{caminho_str}")
        print()
    
    print("Todas as visualizações foram salvas na pasta 'imagens/'")
    return exemplos


if __name__ == "__main__":
    # Executa criação de exemplos se o módulo for executado diretamente
    try:
        criar_visualizacoes_exemplo()
    except Exception as e:
        print(f"Erro ao criar visualizações: {e}")
        print("Certifique-se de que as dependências estão instaladas:")
        print("pip install networkx matplotlib numpy")