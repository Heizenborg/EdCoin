import socket
from Classes.Block import Block
from Server_Actions import ServerActions
import time

def get_line_item(myTransaction):
	txn = myTransaction.split(':')
	txnDict = {'Sender:':txn[0], 'transaction':txn[1]}
	print("transaction:", txn)

	return txnDict


def add_data(myBlock, myTransaction):
	
	print("Index: ", myBlock.index)
	print("Transaction: ", myTransaction)
	line_item = get_line_item(myTransaction)

	myBlock.data.append(line_item)

	print("new line added to ledger")

	for item in myBlock.data:
		print(item)

	return myBlock

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 8888))

s.listen(5)
index = 0

Chain = [ServerActions.create_genesis_block()]

print(Chain)

start_time = time.time()

while True:
	connect, address = s.accept()
	print("Connection Address:" + str(address))

	str_return = "Welcome to my test EdCoin server. Waiting for command."
	connect.sendto(bytes(str_return, 'utf-8'), address)

	str_recv, temp = connect.recvfrom(1024)
	print(str(str_recv))

	if str(str_recv) == "b'MAKE A BLOCK'":
		next_block = ServerActions.next_block(Chain[index])
		Chain.append(next_block)
		index += 1
		print(Chain)
	if "exit" in str(str_recv):
		pass 
	if "build" in str(str_recv):
		print("BUILD CONTRACT")
		contract = ServerActions.make_new_contract(str(str_recv.decode('ascii')))
		Chain[index].data.append(contract)

		for item in Chain[index].data:
			print(item)
	else:
		Chain[index] = add_data(Chain[index], str_recv.decode('ascii'))
		

	str_return = "Your transaction has been added to the ledger"

	connect.sendto(bytes(str_return, 'utf-8'), address)

	connect.close()
