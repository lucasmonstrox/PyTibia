from utils import utils
from wiki import creatures
import numpy as np

# creatures.creatures = ['A Greedy Eye']

messLetters = ['t', 'T', 'r', 'R', 'f', 'F', 'L']

# (previousLetter == 't' or previousLetter == 'T' or previousLetter == 'r' or previousLetter == 'R' or previousLetter == 'f' or previousLetter == 'F' or previousLetter == 'L') or (letter == 't' or letter == 'T' or letter == 'f' or letter == 'F')

for monster in creatures.creatures:
    monsterLetters = np.zeros((11, 0), dtype=np.uint8)
    for index, letter in enumerate(monster):
        letter = letter if letter != ' ' else 'space'
        letter = letter if letter != '.' else 'dot'
        letterBasePath = 'hud/images/letters/uppercase' if letter.isupper() else 'hud/images/letters/lowercase'
        letterFullPath = '{0}/{1}.png'.format(letterBasePath, letter)
        letterAsArray = utils.loadImgAsArray(letterFullPath).copy()
        letterAsArray[np.nonzero(letterAsArray == 0)] = 1
        letterAsArray[np.nonzero(letterAsArray == 255)] = 0
        # print(letter)
        if index > 0:
            previousLetter = monster[index - 1]
            previousLetterIsMessLetter = (previousLetter == 't' or previousLetter == 'T' or previousLetter == 'r' or previousLetter == 'R' or previousLetter == 'f' or previousLetter == 'F' or previousLetter == 'L')
            letterIsMessLetter = (letter == 't' or letter == 'T' or letter == 'f' or letter == 'F')
            if previousLetterIsMessLetter or letterIsMessLetter:
                size = 2 if previousLetterIsMessLetter and letterIsMessLetter else 1
                ultimaFileiraDaImagem = monsterLetters[:, monsterLetters.shape[1] - size:monsterLetters.shape[1]]
                primeiraFileiraDaProximaLetra = letterAsArray[:, 0:size]
                # if size == 2:
                #     utils.saveImg(np.array(np.where(ultimaFileiraDaImagem == 1, 0, 255), dtype=np.uint8), 'ultimaFileiraDaImagem.png')
                #     utils.saveImg(np.array(np.where(primeiraFileiraDaProximaLetra == 1, 0, 255), dtype=np.uint8), 'primeiraFileiraDaProximaLetra.png')
                # utils.saveImg(primeiraFileiraDaProximaLetra, 'primeiraFileiraDaProximaLetra.png')
                somaDasDuas = np.add(ultimaFileiraDaImagem, primeiraFileiraDaProximaLetra)
                monsterLetters = monsterLetters[:, 0:monsterLetters.shape[1] - size]
                monsterLetters = np.hstack((monsterLetters, somaDasDuas))
                restoDaProximaLetra = letterAsArray[:, size:letterAsArray.shape[0] - 1]
                monsterLetters = np.hstack((monsterLetters, restoDaProximaLetra))
            else:
                monsterLetters = np.hstack((monsterLetters, letterAsArray)) 
        else:
            monsterLetters = np.hstack((monsterLetters, letterAsArray))
    # break
    monsterLetters[np.nonzero(monsterLetters == 0)] = 255
    monsterLetters[np.nonzero(monsterLetters == 1)] = 0
    monsterLetters[np.nonzero(monsterLetters == 2)] = 0
    utils.saveImg(monsterLetters, 'hud/images/monsters/{}.png'.format(monster))
    # break