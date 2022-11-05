# strng = ''
# cnt = 0
# for i in range(1, 201):
#     strng += str(i)
#     if '6' in str(i):
#         cnt = cnt + str(i).count('6')
#         if cnt == 15:
#             print(f'Победа! {cnt}, {i}, {len(strng)}')
#         print(cnt, i, len(strng))

# print('\t', end='')
# for i in range(8):
#     print(i, end='\t')
# for i in range(8):
#     print('\n', i, end='\t')
#     for j in range(8):
#         print((str(oct(i * j)))[2:], end='\t')

test_tup = []
for i in range(4):
    test_tup += f'{str(i)}'
test_tup = tuple(test_tup[:])
print(test_tup)
