from buss import Buss

def hovedprogram():
    #Let's make the buss!
    bus1 = Buss(20)

    for i in range(10):
        bus1.plukk_opp()

    for i in range(12):
        bus1.plukk_opp()

    for i in range(18):
        bus1.slipp_av()

    for i in range(3):
        bus1.slipp_av()

hovedprogram()