import TegComms


def bp(q):
    p1 = 'Что именно тебя интересует? Выбери номер! (для выхода из выбора команды напиши "!бот выход")\n'
    p2 = ''
    p3 = 'Для перехода вперёд: >\nДля перехода назад: <'
    if q == 0:
        for i in range(0, 30):
            p2 += str(i+1) + ': ' + TegComms.tc[i][0] + '\n'

    elif q == 1:
        for i in range(30, 60):
            p2 += str(i+1) + ': ' + TegComms.tc[i][0] + '\n'

    else:
        for i in range(60, len(TegComms.tc)):
            p2 += str(i+1) + ': ' + TegComms.tc[i][0] + '\n'

    return p1+p2+p3



