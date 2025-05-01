import csv

# Клас Block
class Block:
    def __init__(self, id, view):
        self.id = id
        self.view = int(view)

    def __repr__(self):
        return f"Block(id='{self.id}', view={self.view})"

# Клас Vote (не використовується напряму, але можна розширити)
class Vote:
    def __init__(self, block_id):
        self.block_id = block_id

    def __repr__(self):
        return f"Vote(block_id='{self.block_id}')"

# Клас Chain
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

# Зчитування блоків із CSV
def read_blocks_from_csv(filename):
    blocks = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            blocks.append(Block(row['id'], row['view']))
    return blocks

# Зчитування голосів із CSV
def read_votes_from_csv(filename):
    votes = set()
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            votes.add(row['block_id'])
    return votes

# Запис ланцюга у CSV
def write_chain_to_csv(filename, chain):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'view']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for block in chain.blocks:
            writer.writerow({'id': block.id, 'view': block.view})

# Клас вузла дерева
class BSTNode:
    def __init__(self, block):
        self.block = block
        self.left = None
        self.right = None

# Вставка у BST
def insert_bst(root, block):
    if root is None:
        return BSTNode(block)
    if block.view < root.block.view:
        root.left = insert_bst(root.left, block)
    else:
        root.right = insert_bst(root.right, block)
    return root

# Перевірка на повне дерево
def is_full_tree(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    if node.left and node.right:
        return is_full_tree(node.left) and is_full_tree(node.right)
    return False

# Перевірка на ідеальне дерево
def is_perfect_tree(root):
    def depth(node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d

    def check_perfect(node, d, level=0):
        if node is None:
            return True
        if not node.left and not node.right:
            return d == level + 1
        if not node.left or not node.right:
            return False
        return check_perfect(node.left, d, level + 1) and check_perfect(node.right, d, level + 1)

    d = depth(root)
    return check_perfect(root, d)

# Обходи дерева
def preorder(node):
    if node:
        print(node.block)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.block)
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.block)

# Основна програма
if __name__ == "__main__":
    blocks_filename = 'blocks.csv'
    votes_filename = 'votes.csv'
    chain_filename = 'chain.csv'

    # Зчитування блоків і голосів
    blocks = read_blocks_from_csv(blocks_filename)
    votes = read_votes_from_csv(votes_filename)

    # Побудова ланцюга
    chain = Chain()
    for block in blocks:
        chain.add_block(block, votes)

    # Запис результату
    write_chain_to_csv(chain_filename, chain)

    print("Побудований ланцюг:")
    for block in chain.blocks:
        print(block)

    # Побудова дерева з chain.csv
    chain_blocks = read_blocks_from_csv(chain_filename)

    root = None
    for block in chain_blocks:
        root = insert_bst(root, block)

    # Визначення типу дерева
    print("\nТип дерева:")
    if is_perfect_tree(root):
        print("Дерево є ідеальним (perfect).")
    elif is_full_tree(root):
        print("Дерево є повним (full).")
    else:
        print("Дерево не є ні повним, ні ідеальним.")

    # Обходи
    print("\nОбхід у прямому порядку (preorder):")
    preorder(root)

    print("\nОбхід у порядку (inorder):")
    inorder(root)

    print("\nОбхід у зворотному порядку (postorder):")
    postorder(root)
