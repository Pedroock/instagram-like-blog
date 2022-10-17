from pairing import pair , depair


pk_request = 1
pk_reciever = 2
if pk_request > pk_reciever:
    id = pair(pk_reciever, pk_request)
else: 
    id = pair(pk_request, pk_reciever)

print(id)
print(f'n1 {depair(id)[0]}', f'n2 {depair(id)[1]}')


pk_request = 2
pk_reciever = 1
if pk_request > pk_reciever:
    id = pair(pk_reciever, pk_request)
else: 
    id = pair(pk_request, pk_reciever)

print(id)
print(f'n1 {depair(id)[0]}', f'n2 {depair(id)[1]}')