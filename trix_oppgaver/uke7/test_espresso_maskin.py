from espresso_maskin import Espresso_maskin

maskin = Espresso_maskin(1000)

for i in range(26):
    maskin.lag_espresso()

maskin.fyll_vann(100)

maskin.lag_lungo()

maskin.fyll_vann(10)

maskin.lag_lungo()

assert maskin.hent_vann_mengde() == 0