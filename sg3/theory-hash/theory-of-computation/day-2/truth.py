for A in [False, True]:
    for B in [False, True]:
        for C in [False, True]:
            print(
                f'{int(A)} -- {int(B)} -- {int(C)} -- {int((A or B) or ( (not A and C) and not (B or C) ))}')
