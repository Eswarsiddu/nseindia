from dependencies.Constants import Constants as Const

d = {Const.DEFAULT: None, Const.SAVED_VALUES: None}
d[Const.DEFAULT] = {
    Const.CALLS: {Const.OI: {Const.NIFTY: 1, Const.BANK_NIFTY: 1},
                  Const.CHANGE_IN_OI: {Const.NIFTY: 2, Const.BANK_NIFTY: 2},
                  Const.LTP: {Const.NIFTY: 6, Const.BANK_NIFTY: 6},
                  Const.TRENDS1: {Const.NIFTY: 3, Const.BANK_NIFTY: 3},
                  Const.TRENDS2: {Const.NIFTY: 4, Const.BANK_NIFTY: 4},
                  Const.TRENDS3: {Const.NIFTY: 5, Const.BANK_NIFTY: 5},
                  Const.CALLS: {Const.NIFTY: 1, Const.BANK_NIFTY: 1}
                  },
    Const.PUTS: {Const.OI: {Const.NIFTY: 2, Const.BANK_NIFTY: 2},
                 Const.CHANGE_IN_OI: {Const.NIFTY: 3, Const.BANK_NIFTY: 3},
                 Const.LTP: {Const.NIFTY: 1, Const.BANK_NIFTY: 1},
                 Const.TRENDS1: {Const.NIFTY: 4, Const.BANK_NIFTY: 4},
                 Const.TRENDS2: {Const.NIFTY: 5, Const.BANK_NIFTY: 5},
                 Const.TRENDS3: {Const.NIFTY: 6, Const.BANK_NIFTY: 6},
                 Const.PUTS: {Const.NIFTY: 3, Const.BANK_NIFTY: 3}
                 },
    Const.STRIKE_PRICE: {Const.NIFTY: 2, Const.BANK_NIFTY: 2}
}
d[Const.SAVED_VALUES] = {
    Const.CALLS: {Const.OI: {Const.NIFTY: 1, Const.BANK_NIFTY: 1},
                  Const.CHANGE_IN_OI: {Const.NIFTY: 2, Const.BANK_NIFTY: 2},
                  Const.LTP: {Const.NIFTY: 6, Const.BANK_NIFTY: 6},
                  Const.TRENDS1: {Const.NIFTY: 3, Const.BANK_NIFTY: 3},
                  Const.TRENDS2: {Const.NIFTY: 4, Const.BANK_NIFTY: 4},
                  Const.TRENDS3: {Const.NIFTY: 5, Const.BANK_NIFTY: 5},
                  Const.CALLS: {Const.NIFTY: 1, Const.BANK_NIFTY: 1}
                  },
    Const.PUTS: {Const.OI: {Const.NIFTY: 2, Const.BANK_NIFTY: 2},
                 Const.CHANGE_IN_OI: {Const.NIFTY: 3, Const.BANK_NIFTY: 3},
                 Const.LTP: {Const.NIFTY: 1, Const.BANK_NIFTY: 1},
                 Const.TRENDS1: {Const.NIFTY: 4, Const.BANK_NIFTY: 4},
                 Const.TRENDS2: {Const.NIFTY: 5, Const.BANK_NIFTY: 5},
                 Const.TRENDS3: {Const.NIFTY: 6, Const.BANK_NIFTY: 6},
                 Const.PUTS: {Const.NIFTY: 3, Const.BANK_NIFTY: 3}
                 },
    Const.STRIKE_PRICE: {Const.NIFTY: 2, Const.BANK_NIFTY: 2}
}
t = """{'default': {'CE': {'OI': {0: 1, 1: 1}, 'CHANGEINOI': {0: 2, 1: 2}, 'LTP': {0: 6, 1: 6}, 'trends1': {0: 3, 1: 3}, 'trends2': {0: 4, 1: 4}, 'trends3': {0: 5, 1: 5}, 'CE': {0: 1, 1: 1}}, 'PE': {'OI': {0: 2, 1: 2}, 'CHANGEINOI': {0: 3, 1: 3}, 'LTP': {0: 1, 1: 1}, 'trends1': {0: 4, 1: 4}, 'trends2': {0: 5, 1: 5}, 'trends3': {0: 6, 1: 6}, 'PE': {0: 3, 1: 3}}, 'STRIKE PRICE': {0: 2, 1: 2}}, 'savedvalues': {'CE': {'OI': {0: 1, 1: 1}, 'CHANGEINOI': {0: 2, 1: 2}, 'LTP': {0: 6, 1: 6}, 'trends1': {0: 3, 1: 3}, 'trends2': {0: 4, 1: 4}, 'trends3': {0: 5, 1: 5}, 'CE': {0: 1, 1: 1}}, 'PE': {'OI': {0: 2, 1: 2}, 'CHANGEINOI': {0: 3, 1: 3}, 'LTP': {0: 1, 1: 1}, 'trends1': {0: 4, 1: 4}, 'trends2': {0: 5, 1: 5}, 'trends3': {0: 6, 1: 6}, 'PE': {0: 3, 1: 3}}, 'STRIKE PRICE': {0: 2, 1: 2}}}"""
for i in t:
    if i == "'":
        print('"',end="")
    else:
        print(i, end="")