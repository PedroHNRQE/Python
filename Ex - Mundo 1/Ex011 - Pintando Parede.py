lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
tinta = area / 2
print('Sua parede tem a dimensao de {}x{} e sua area e de {:.2f}m².'.format(lar, alt, area))
print('Para pinta essa parede, voce precisara de {:.2f}l de tinta.'.format(tinta))
