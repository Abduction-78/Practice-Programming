#T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24


messy_string = 'T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24'

split = messy_string.split(' ')

answer = []
for i in range(100):
    answer.append('*')

def join_str(s):
    print(''.join(s))

for p in split:
    first_charater = p[0]
    index = int(p[1:])
    answer[index] = first_charater
    join_str(answer)

join_str(answer)