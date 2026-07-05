import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Configuração das cores 
cor_fundo_fig = '#0a001a' 
cor_fundo_ax = '#140033'  
cor_linha = '#00e5ff'     
cor_limite = '#ff00aa'    

# 2. Configuração principal da janela 
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor(cor_fundo_fig)
ax.set_facecolor(cor_fundo_ax)
plt.subplots_adjust(bottom=0.25)

# 3. Cálculos do Fator de Lorentz
c = 1.0
v = np.linspace(0, 0.999 * c, 1000)
gamma = 1 / np.sqrt(1 - (v**2 / c**2))

# 4. Efeito (Estrelas de várias cores e tamanhos no fundo)
num_estrelas = 250
x_estrelas = np.random.uniform(0, 1.05, num_estrelas)
y_estrelas = np.random.uniform(0, 50, num_estrelas)
tamanhos = np.random.uniform(5, 70, num_estrelas)
cores_estrelas = np.random.choice(['#ffffff', '#ff00aa', '#00e5ff', '#8a2be2'], num_estrelas)
ax.scatter(x_estrelas, y_estrelas, s=tamanhos, c=cores_estrelas, alpha=0.3)

# 5. Plotando a curva e a barreira da luz
ax.plot(v, gamma, color=cor_linha, linewidth=3.5, alpha=0.9, label='Fator de Lorentz')
ax.axvline(x=1.0, color=cor_limite, linestyle='--', linewidth=2.5, label='Limite (Velocidade da Luz)')

# 6. Ponto interativo (Sua partícula)
v_inicial = 0.0
gamma_inicial = 1.0
ponto, = ax.plot([v_inicial], [gamma_inicial], marker='o', color='#ffffff', markeredgecolor=cor_limite, markeredgewidth=2, markersize=14, label='Sua Partícula')

# 7. Ajustando a MAIOR ESCALA
ax.set_xlim(0, 1.05) # Foca bem em cima do limite 1.0
ax.set_ylim(0, 50)   # Eixo Y esticado até 50 para ver o gráfico decolar

# 8. Estilização dos textos e grades
ax.set_title('Simulação: Aumento da Inércia', fontsize=16, fontweight='bold', color='white')
ax.set_xlabel('Fração da Velocidade da Luz (v/c)', fontsize=12, color='white')
ax.set_ylabel('Multiplicador (Fator de Lorentz)', fontsize=12, color='white')
ax.tick_params(colors='white')
ax.grid(True, linestyle='-', alpha=0.15, color='white')

# 9. Estilização da Legenda
leg = ax.legend(facecolor=cor_fundo_ax, edgecolor=cor_limite, fontsize=12, loc='upper left')
for text in leg.get_texts():
    text.set_color("white")

# 10. Configurar Slider com as cores do tema
ax_slider = plt.axes([0.15, 0.1, 0.7, 0.03])
ax_slider.set_facecolor(cor_fundo_ax)
slider = Slider(ax_slider, 'Velocidade', 0.0, 0.999, valinit=v_inicial, color=cor_limite)
slider.label.set_color('white')
slider.valtext.set_color('white')

# 11. Função para animar o movimento
def atualizar(val):
    velocidade_atual = slider.val
    gamma_atual = 1 / np.sqrt(1 - (velocidade_atual**2 / c**2))
    ponto.set_data([velocidade_atual], [gamma_atual])
    fig.canvas.draw_idle()

slider.on_changed(atualizar)

# Exibe na tela
plt.show()