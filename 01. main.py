import hashlib          # Library for Sha256

# Function to generate Hash
def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

# Create a block
class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash

# Create a Blockchain
class Blockchain:
    def __init__(self):
        hashLast = hashGenerator('Vasista')
        hastStart = hashGenerator('Kashyap')

        genesis = Block('gen_data',hastStart, hashLast)
        self.chain = [genesis]                           # My Chain

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data+prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)

Blk_chn = Blockchain()
Blk_chn.add_block('1')
Blk_chn.add_block('2')
Blk_chn.add_block('3')

for block in Blk_chn.chain:
    print(block.__dict__)
