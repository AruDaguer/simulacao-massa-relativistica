import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define a velocidade c como 1
c = 1.0

# Cria o array de velocidades para desenhar a curva base
v = np.linspace(0, 0.999 * c, 1000)
gamma = 1 / np.sqrt(1 - (v**2 / c**2))

# Configuração principal da janela do gráfico
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25) # Deixa um espaço em branco na parte de baixo para o slider

# Desenha a linha da curva e a linha pontilhada da velocidade da luz
ax.plot(v, gamma, color='blue', linewidth=2, alpha=0.5, label='Fator de Lorentz')
ax.axvline(x=1.0, color='red', linestyle='--', linewidth=2, label='Limite (Velocidade da Luz)')

# Cria um ponto vermelho que vai se mover pelo gráfico
v_inicial = 0.0
gamma_inicial = 1.0
ponto, = ax.plot([v_inicial], [gamma_inicial], 'ro', markersize=10, label='Sua Partícula')

# Estilização
ax.set_title('Simulação: Aumento da Inércia', fontsize=14, fontweight='bold')
ax.set_xlabel('Fração da Velocidade da Luz (v/c)', fontsize=12)
ax.set_ylabel('Multiplicador (Fator de Lorentz)', fontsize=12)
ax.set_xlim(0, 1.1)
ax.set_ylim(0, 25)
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend()

# Cria o eixo e o Slider na parte de baixo da tela
ax_slider = plt.axes([0.15, 0.1, 0.7, 0.03])
slider = Slider(ax_slider, 'Velocidade', 0.0, 0.999, valinit=v_inicial, color='green')

# Função que atualiza a posição do ponto vermelho quando você arrasta o slider
def atualizar(val):
    velocidade_atual = slider.val
    gamma_atual = 1 / np.sqrt(1 - (velocidade_atual**2 / c**2))
    ponto.set_data([velocidade_atual], [gamma_atual])
    fig.canvas.draw_idle()

# Conecta o slider à função de atualização
slider.on_changed(atualizar)

# Mostra o gráfico interativo
plt.show()