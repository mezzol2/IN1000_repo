print("Tast inn din inntekt:")
inntekt = int(input())

skatt = inntekt * .1

if inntekt >= 10000:
    skatt = skatt + (inntekt - 10000) * .3

print(f'Skatt: {skatt}')