# Trabalho 2 de Sistemas Operacionais - Samuel Silveira Pordeus - 11400947

import math

# Lendo o arquivo de entrada
otm_list, fifo_list, lru_list = [], [], []
file = open('entrada.txt')
for line in file.readlines():
    fifo_list.append(int(line))
    otm_list.append(int(line))
    lru_list.append(int(line))
index = fifo_list[0]
fifo_list.pop(0)
otm_list.pop(0)
lru_list.pop(0)


def FIFO(pages_list, index):
    pos = 0
    fault = 0
    frame = [None for x in range(index)]
    for x in range(len(pages_list)):
        if pages_list[x] not in frame:
            fault += 1
            frame[pos] = pages_list[x]
            pos += 1
            if pos >= index:
                pos = 0
    print("FIFO:", fault)


def OTM(pages_list, index):

    aux_list = pages_list
    fault = 0
    pages_list = [[pages_list[x], None] for x in range(len(pages_list))]
    frame = [[math.inf, math.inf] for x in range(index)]

    # Setando as distancias
    for x in range(len(pages_list)):
        page_aux = [i for i, c in enumerate(aux_list) if c == pages_list[x][0]]
        try:
            pages_list[x][1] = x + page_aux[1]
            aux_list.pop(aux_list.index(pages_list[x][0]))
            page_aux.pop(0)
        except:
            pages_list[x][1] = math.inf
    for x in range(len(pages_list)):
        if not pages_list[x][1]:
            pages_list[x][1] = math.inf

    # Calculando as faltas
    for x in range(len(pages_list)):
        is_not_on_list = 0
        for sublist in frame:
            if pages_list[x][0] != sublist[0]:
                is_not_on_list += 1 # If its not on list, it has the size of index - so we can insert the new one
        if is_not_on_list == index:
            fault += 1 # Replacing
            del frame[index - 1]
            frame.insert(index, pages_list[x])
            frame.sort(key=lambda x: x[1])
        else:
            for sublist in frame:
                if pages_list[x][0] == sublist[0]:
                    sublist[1] = math.inf

    print("OTM:", fault)


def LRU(pages_list, index):
    pos = 0
    fault = 0
    frame = [None for x in range(index)]
    for x in range(len(pages_list)):
        if pages_list[x] not in frame:
            fault += 1
            frame.pop(0)
            frame.insert(index, pages_list[x])
            pos += 1
            if pos >= index:
                pos = 0
        else:
            frame.pop(frame.index(pages_list[x]))
            frame.insert(index, pages_list[x])
    print("LRU:", fault)


FIFO(fifo_list, index)
OTM(otm_list, index)
LRU(lru_list, index)
