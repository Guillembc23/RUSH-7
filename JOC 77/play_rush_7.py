import random

GUARDADES = 2


def play(jugador1,jugador2, imprimir = True):
    deck = [f"{rank}{suit}" for rank in "01234567" for suit in "♠♥♦♣"]
    random.shuffle(deck)

    enjoc = 5*[True]
    n_enjoc = 5

    mano1 = [deck.pop() for _ in range(GUARDADES)]
    mano2 = [deck.pop() for _ in range(GUARDADES)]

    extra1 = [0 for _ in range(0,5)]
    extra2 = [0 for _ in range(0,5)]

    nombre1 = [0 for _ in range(0,5)]
    nombre2 = [0 for _ in range(0,5)]

    control1 = [['  ' for _ in range(0,4)] for _ in range(0,5)]
    control2 = [['  ' for _ in range(0,4)] for _ in range(0,5)]

    wins1 = 0
    wins2 = 0

    def punt(card):
        return ord(card[0])-ord('0')

    def punt_par(card):
        return punt(card)//3
    
    #bucle de joc
    while True:
        if wins1 >= 3:
            if imprimir:
                print('GANA JUGADOR 1'+ f" ({wins1} - {wins2})")
            return 1
        elif wins2 >= 3:
            if imprimir:
                print('GANA JUGADOR 2'+ f" ({wins1} - {wins2})")
            return 2
        
        random.shuffle(deck)
        random.shuffle(deck)
        for _ in range(0,n_enjoc):
            mano1.append(deck.pop())
            mano2.append(deck.pop())


        mano1, juga1 = jugador1(mano1,control1,control2,extra1,extra2,nombre1,nombre2,enjoc,n_enjoc)
        mano2, juga2 = jugador2(mano2,control2,control1,extra2,extra1,nombre2,nombre1,enjoc,n_enjoc)

        if (len(juga1) != n_enjoc or len(juga2) != n_enjoc): 
            print('ERROR DE ENTRADA')
            return

            
        for i in range(0,5):
            if enjoc[i]:
                punt1 = extra1[i] + punt(juga1[0])
                punt2 = extra2[i] + punt(juga2[0])

                if (punt1 > punt2):
                    for j in range(0,4):
                        if control1[i][j] == '  ':
                            control1[i][j] = juga2[0]
                            if j == 3:
                                enjoc[i] = False
                                n_enjoc -= 1
                                wins1 += 1
                            break
                    extra1[i] += punt_par(juga2[0])
                    extra2[i] = 0
                    nombre1[i] += 1
                    nombre2[i] = 0
                    for j in range(0,4):
                        if control2[i][j] != '  ':
                            deck.append(control2[i][j])
                            control2[i][j] = '  '
                    deck.append(juga1[0])

                elif(punt1 < punt2):
                    for j in range(0,4): 
                        if control2[i][j] == '  ':
                            control2[i][j] = juga1[0]
                            if j == 3:
                                enjoc[i] = False
                                n_enjoc -= 1
                                wins2 += 1
                            break
                    extra2[i] += punt_par(juga1[0])
                    extra1[i] = 0
                    nombre2[i] += 1
                    nombre1[i] = 0

                    for j in range(0,4):
                        if control1[i][j] != '  ':
                            deck.append(control1[i][j])
                            control1[i][j] = '  '
                    deck.append(juga2[0])
                
                else:
                    deck.append(juga1[0])
                    deck.append(juga2[0])

                juga1.pop(0)
                juga2.pop(0)
    return 0

def enfrentar(jugador1,jugador2,N = 4):
    jocs1 = 0
    jocs2 = 0
    for i in range(0,10**N):
        res = play(jugador1,jugador2,False)
        if res == 1:
            jocs1 += 1
        elif res == 2:
            jocs2 += 1
    print('RESULTAT: ' + f"({jocs1} - {jocs2})")
