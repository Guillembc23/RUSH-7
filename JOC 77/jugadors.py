from play_rush_7 import *

from manual import *

def jugador_random(mano,control1,control2,extra1,extra2,nombre1,nombre2,enjoc,n_enjoc):
    random.shuffle(mano)
    juga = mano[0:n_enjoc]
    mano = mano[n_enjoc:n_enjoc+GUARDADES]
    return mano, juga

def jugador_guarda(mano,control1,control2,extra1,extra2,nombre1,nombre2,enjoc,n_enjoc):
    mano.sort()
    if n_enjoc == 5: #guardar millors
        juga = mano[0:n_enjoc]
        mano = mano[n_enjoc:n_enjoc+GUARDADES]
    else: #guardar pitjors
        juga = mano[GUARDADES:n_enjoc+GUARDADES]
        mano = mano[0:GUARDADES]
    random.shuffle(juga)
    return mano, juga

def jugador_ordena(mano,control1,control2,extra1,extra2,nombre1,nombre2,enjoc,n_enjoc):
    mano.sort()
    estat = [[extra1[i]-extra2[i],nombre1[i]+nombre2[i],'  ',random.randint(0,20),i] for i in range(0,5) if enjoc[i]]
    estat.sort()
    if n_enjoc == 5:
        quasi_juga = [[tup[4],mano.pop(0)] for tup in estat]
    else:
        quasi_juga = [[tup[4],mano.pop(GUARDADES)] for tup in estat]
    quasi_juga.sort()
    juga = [tup[1] for tup in quasi_juga]
    return mano, juga


def jugador_prioritza(mano,control1,control2,extra1,extra2,nombre1,nombre2,enjoc,n_enjoc):
    mano.sort()
    guanyades = sum([1 for tup in nombre1 if tup == 4])
    perdudes = (5 - n_enjoc) - guanyades
    restants_males = 2 - perdudes
    restants_bones = 3 - guanyades

    estat = [[extra1[i]-extra2[i],nombre1[i]+nombre2[i],'  ',random.randint(0,20),i] for i in range(0,5) if enjoc[i]]
    estat.sort()

    quasi_juga = [[estat[j][4],mano.pop(restants_males-1-j)] for j in range(0,restants_males)]+[[estat[restants_males+j][4],mano.pop()] for j in range(0,restants_bones)]
    quasi_juga.sort()
    juga = [tup[1] for tup in quasi_juga]
    return mano, juga




play(jugador_manual,jugador_prioritza,imprimir = False)