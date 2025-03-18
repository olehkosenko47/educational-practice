import csv

class Block:
    def __init__(self, id, view):
        self.id = id
        self.view = int(view)

    def __repr__(self):
        return f"Block(id='{self.id}', view={self.view})"

class Vote:
    def __init__(self, block_id):
        self.block_id = block_id

    def __repr__(self):
        return f"Vote(block_id='{self.block_id}')"

class Chain:
    def __init__(self):
        self.blocks = []

    def get_tip(self):
        return self.blocks[-1] if self.blocks else None

    def is_valid_addition(self, block, votes):
        if not votes or block.id not in votes:
            return False
        tip = self.get_tip()
        if tip is None:
            return block.view == 0
        return block.view == tip.view + 1

    def add_block(self, block, votes):
        if self.is_valid_addition(block, votes):
            self.blocks.append(block)
            return True
        return False

def read_blocks_from_csv(filename):
    blocks = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            blocks.append(Block(row['id'], row['view']))
    return blocks

def read_votes_from_csv(filename):
    votes = set()
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            votes.add(row['block_id'])
    return votes

def write_chain_to_csv(filename, chain):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'view']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for block in chain.blocks:
            writer.writerow({'id': block.id, 'view': block.view})

if __name__ == "__main__":
    blocks_filename = 'blocks.csv'
    votes_filename = 'votes.csv'
    chain_filename = 'chain.csv'

    blocks = read_blocks_from_csv(blocks_filename)
    votes = read_votes_from_csv(votes_filename)

    chain = Chain()

    for block in blocks:
        chain.add_block(block, votes)

    write_chain_to_csv(chain_filename, chain)

    print("Побудований ланцюг:")
    for block in chain.blocks:
        print(block)