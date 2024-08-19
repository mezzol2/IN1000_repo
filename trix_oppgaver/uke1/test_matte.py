rsvar = "Riktig!"
fsvar = "Beklager, det var feil. Spillet er over."
endsvar = "Gratulerer, du vant!"

a = 1
b = 2
func = "+"
q_prompt = f"Hva er {a} {func} {b}? "
svar1 = input(q_prompt)

if svar1 == str(a + b):
    print(rsvar)
    #go further

    a = a + 1
    b = b + 2
    func = "-"
    q_prompt = f"Hva er {a} {func} {b}? "
    svar1 = input(q_prompt)

    if svar1 == str(a - b):
        print(rsvar)
        #we must go deeper

        a = a + 1
        b = b + 2
        func = "*"
        q_prompt = f"Hva er {a} {func} {b}? "
        svar1 = input(q_prompt)

        if svar1 == str(a * b):
            print(endsvar)
        else: 
            print(fsvar)

    else:
        print(fsvar)

else:
    print(fsvar)