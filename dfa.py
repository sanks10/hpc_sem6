dfa101 = {0:{'1':1},
       1:{'0':2},
       2:{'1':3},
       3:{'0':3, '1':3}}

dfa001={0:{'0':1},
       1:{'0':2},
       2:{'1':3},
       3:{'0':3, '1':3}}

def accepts(transitions,initial,accepting,s):
    state = initial
    try:
        for c in s:
            state = transitions[state][c]
        if(state in accepting):
            return 'Accepted'
        else:
            return 'Rejected'
    except:
        return 'Rejected'
print('Dfa of 101+ ',accepts(dfa101,0,{3},'00101111000'))
print('Dfa of 001+ ',accepts(dfa001,0,{3},'00101010101'))
