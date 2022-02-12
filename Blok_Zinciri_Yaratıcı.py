from encodings import utf_8
from hashlib import sha256

def updatehash(*args):
    hashing_text = ""; h = sha256()
    for arg in args:
        hashing_text += str(arg)
    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

class Block():
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64 

    def __init__(self, data, number = 0):
        self.data = data
        self.number = number

    def hash(self):
        return updatehash(
            self.previous_hash, 
            self.number, 
            self.data, 
            self.nonce
            )

    def __str__(self):
        return str("Block#: %s\nHash: %s\nPrevious:" +
        "%s\nData: %s\nNonce: %s\n") %(
        self.number,
        self.hash(), 
        self.previous_hash,
        self.data,
        self.nonce
        )

class Blockchain():
    zorluk = 4

    def __init__(self, chain=[]):
        self.chain=chain
    
    def add(self, block):
        self.chain.append({
            'hash': block.hash(),
            'previous': block.previous_hash, 
            'number': block.number, 
            'data': block.data, 
            'nonce': block.nonce})

    def remove(self, block):
        self.chain.remove(block)

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].get('hash')
        except IndexError:
            pass
        while True:
            if block.hash()[:self.zorluk] == "0" * self.zorluk:
                self.add(block); break
            else:
                block.nonce += 1  


def main():
    blockchain  = Blockchain()
    database = []
    uzunluk = int(input("Kaç blokluk bir zincir oluşturacaksınız? "))
    i = 0
    while i < uzunluk:
        veri = input("Veri giriniz: ")
        database.append(veri)
        i += 1
        
    no = 0
    for data in database:
        no += 1
        blockchain.mine(Block(data,no))

    for block in blockchain.chain:
        print(block)

if __name__ == '__main__':
    main()

input('Programı kapatmak için "Enter" tuşuna basınız.')