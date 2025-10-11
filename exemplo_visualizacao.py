"""
Exemplo simples de uso do módulo de visualização.

Este arquivo demonstra como usar o VisualizadorGrafo diretamente
para criar visualizações personalizadas.
"""

from main import Grafo, CaminhoHamiltoniano
from view import VisualizadorGrafo

def exemplo_uso_visualizacao():
    """
    Demonstra o uso básico do sistema de visualização.
    """
    print("Exemplo de uso do módulo de visualização")
    print("="*50)
    
    # Criar um grafo simples
    grafo = Grafo(4, orientado=False)
    
    # Adicionar arestas para formar um quadrado com uma diagonal
    arestas = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
    
    for origem, destino in arestas:
        grafo.adicionar_aresta(origem, destino)
    
    print("Grafo criado:")
    grafo.imprimir_grafo()
    
    # Buscar caminho hamiltoniano
    algoritmo = CaminhoHamiltoniano(grafo)
    encontrou, caminho = algoritmo.encontrar_caminho()
    
    if encontrou:
        print(f"\nCaminho Hamiltoniano: {' → '.join(map(str, caminho))}")
    else:
        print("\nNenhum caminho hamiltoniano encontrado")
    
    # Criar visualização
    visualizador = VisualizadorGrafo(grafo)
    
    print("\nCriando visualização...")
    arquivo = visualizador.visualizar_grafo_completo(
        caminho=caminho if encontrou else None,
        titulo="Exemplo Personalizado - Grafo Quadrado",
        layout='circular',
        nome_arquivo="exemplo_personalizado",
        mostrar=False
    )
    
    if arquivo:
        print(f"Visualização salva em: {arquivo}")
    else:
        print("Erro ao criar visualização")

if __name__ == "__main__":
    try:
        exemplo_uso_visualizacao()
    except ImportError as e:
        print(f"Erro de importação: {e}")
        print("Certifique-se de instalar as dependências:")
        print("pip install -r requirements.txt")
    except Exception as e:
        print(f"Erro: {e}")