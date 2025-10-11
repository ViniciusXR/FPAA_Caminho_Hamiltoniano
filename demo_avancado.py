"""
Demonstração programática do sistema de visualização.

"""

from main import Grafo, CaminhoHamiltoniano
from view import VisualizadorGrafo

def demo_uso_programatico():
    """
    Demonstra uso programático avançado do sistema de visualização.
    """
    print("Demonstração de Uso Programático")
    print("="*40)
    
    # Exemplo 1: Grafo em cadeia
    print("\n1. Criando grafo em cadeia (linha)")
    grafo_linha = Grafo(5, orientado=False)
    for i in range(4):
        grafo_linha.adicionar_aresta(i, i + 1)
    
    algoritmo1 = CaminhoHamiltoniano(grafo_linha)
    encontrou1, caminho1 = algoritmo1.encontrar_caminho()
    
    if encontrou1:
        visualizador1 = VisualizadorGrafo(grafo_linha)
        
        # Personalizar configurações
        visualizador1.config['node_color'] = '#FFB6C1'  # Rosa claro
        visualizador1.config['path_color'] = '#8B0000'   # Vermelho escuro
        visualizador1.config['node_size'] = 1200
        
        arquivo1 = visualizador1.visualizar_grafo_completo(
            caminho=caminho1,
            titulo="Grafo Linear - Demonstração",
            layout='spring',
            nome_arquivo="demo_grafo_linear",
            mostrar=False
        )
        print(f"✓ Grafo linear salvo: {arquivo1}")
    
    # Exemplo 2: Grafo estrela
    print("\n2. Criando grafo estrela")
    grafo_estrela = Grafo(6, orientado=False)
    centro = 0
    for i in range(1, 6):
        grafo_estrela.adicionar_aresta(centro, i)
    
    algoritmo2 = CaminhoHamiltoniano(grafo_estrela)
    encontrou2, caminho2 = algoritmo2.encontrar_caminho()
    
    visualizador2 = VisualizadorGrafo(grafo_estrela)
    arquivo2 = visualizador2.visualizar_grafo_completo(
        caminho=caminho2 if encontrou2 else None,
        titulo="Grafo Estrela - Sem Caminho Hamiltoniano",
        layout='circular',
        nome_arquivo="demo_grafo_estrela",
        mostrar=False
    )
    
    status2 = "encontrado" if encontrou2 else "NÃO encontrado"
    print(f"✓ Grafo estrela salvo: {arquivo2} (Caminho {status2})")
    
    # Exemplo 3: Grafo cíclico
    print("\n3. Criando grafo cíclico")
    grafo_ciclo = Grafo(6, orientado=False)
    vertices = list(range(6))
    for i in range(6):
        grafo_ciclo.adicionar_aresta(vertices[i], vertices[(i + 1) % 6])
    
    algoritmo3 = CaminhoHamiltoniano(grafo_ciclo)
    encontrou3, caminho3 = algoritmo3.encontrar_caminho()
    
    if encontrou3:
        visualizador3 = VisualizadorGrafo(grafo_ciclo)
        
        # Configuração especial para ciclos
        visualizador3.config['figure_size'] = (10, 10)
        visualizador3.config['path_width'] = 6
        
        arquivo3 = visualizador3.visualizar_grafo_completo(
            caminho=caminho3,
            titulo="Grafo Cíclico - Hexágono",
            layout='circular',
            nome_arquivo="demo_grafo_ciclico",
            mostrar=False
        )
        print(f"✓ Grafo cíclico salvo: {arquivo3}")
    
    print(f"\n🎨 Total de demonstrações criadas: 3")
    print("📁 Arquivos salvos na pasta 'assets/'")

def demo_layouts():
    """
    Demonstra diferentes tipos de layout disponíveis.
    """
    print("\nDemonstração de Layouts Diferentes")
    print("="*35)
    
    # Criar um grafo de teste
    grafo = Grafo(5, orientado=False)
    arestas = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 3)]
    for origem, destino in arestas:
        grafo.adicionar_aresta(origem, destino)
    
    algoritmo = CaminhoHamiltoniano(grafo)
    encontrou, caminho = algoritmo.encontrar_caminho()
    
    layouts = ['spring', 'circular', 'kamada_kawai', 'spectral']
    
    for layout in layouts:
        print(f"Criando layout: {layout}")
        
        visualizador = VisualizadorGrafo(grafo)
        arquivo = visualizador.visualizar_grafo_completo(
            caminho=caminho if encontrou else None,
            titulo=f"Layout: {layout.title()}",
            layout=layout,
            nome_arquivo=f"demo_layout_{layout}",
            mostrar=False
        )
        
        if arquivo:
            print(f"✓ Layout {layout} salvo: {arquivo}")
        else:
            print(f"✗ Erro ao criar layout {layout}")

if __name__ == "__main__":
    try:
        demo_uso_programatico()
        demo_layouts()
        
        print("\n" + "="*50)
        print("DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
        print("="*50)
        print("\nVerifique a pasta 'assets/' para ver todas as visualizações geradas.")
        
    except ImportError as e:
        print(f"Erro de importação: {e}")
        print("Instale as dependências: pip install -r requirements.txt")
    except Exception as e:
        print(f"Erro na demonstração: {e}")