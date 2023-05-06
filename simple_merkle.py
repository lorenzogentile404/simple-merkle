import hashlib
import math

# Reference https://blockchain-academy.hs-mittweida.de/merkle-tree/

# Params for visualization purposes
HASH_TRUNC = 5

# Supporting function to compute hash
def h(v):
    return hashlib.sha256(v.encode('utf-8')).hexdigest()

# Supporting function to print the tree decently
def print_tree(tree):
    print("tree =")  
    for i in range(len(tree)-1,0,-1):
        layer = tree[i]
        print("layer " + str(i) + ": " + ' '.join([l[0:HASH_TRUNC] + "..." for l in layer])) # Print only prefix of hashes
    print("layer 0: " + ' '.join(tree[0]) + "\n")

# Given the leaves of the tree, compute all the layers of the merkle tree
def compute_tree(leaves):    
    # Supporting functions    
    # Given a layer of the tree, possibly duplicate last element to ensure even len
    even = lambda layer : layer + [layer[-1]] if len(layer) % 2 != 0 else layer
    # Given a layer of the tree, compute the upper layer
    upper = lambda layer : [h(layer[i] + layer[i+1]) for i in range(0,len(layer),2)]  
        
    # Ensure number of leaves is even
    leaves = even(leaves)
    # Compute hash of each leaf
    layer = [h(l) for l in leaves]
    # Init tree
    tree = [leaves,layer]    
    # Compute layers up to the root
    while len(layer) > 1:
        # Compute the upper layer        
        layer = upper(layer)
        if len(layer) != 1:
            layer = even(layer)
        tree += [layer]
    # Return tree and root
    return tree,layer[0]

# Given an element of the tree, verify if a given inclusion proof is valid
def verify_proof(element,root,proof):
    # Compute hash of the element
    h_verify = h(element)
    # Combine hashes representing the proof
    for h_proof in proof:
        # Concatenation is not commutative, so check if proof element is a right node (wrt to parent)
        h_verify = h(h_verify + h_proof[0]) if h_proof[1] else h(h_proof[0] + h_verify)

    # Check if the root of the tree is obtained
    print("obtained root = " + h_verify)
    print(h_verify == root)
    return h_verify == root

# Given an element and a tree, compute a proof that the element is included in the leaves
def compute_proof(element,tree):
    # Supporting functions    
    # Given the index of an element, return the index of the sibling
    sibling_index = lambda i: i + 1 if i % 2 == 0 else i - 1
    
    # Get the index of the first occurence of the element
    i = tree[0].index(element)    
    
    # Here the case of element not in the tree should be handled
    
    proof = []    
    print("proof = ")
    for j in range(1,len(tree)-1):
        if j > 1:
            # Get the index of the parent
            i = math.floor(i / 2)
        # Get the index of the sibling of the parent
        i = sibling_index(i)
        # Get the element of the proof and indicate if it is a right node (wrt to parent)
        proof += [(tree[j][i], i % 2 != 0)]        
        print("tree[" + str(j) + "][" + str(i) + "] = " + tree[j][i][0:HASH_TRUNC] + "...")
    return(proof)

# Compute tree and root starting from leaves
leaves = ["000","001","010","011","100","101"]
tree,root = compute_tree(leaves)

print_tree(tree)
print("root = " + root)
    
# Check if computed proofs are valid
for i in range(0,len(leaves)):
    print("\ncheck tree[0][" + str(i) + "] = " + leaves[i])
    assert(verify_proof(leaves[i],root,compute_proof(leaves[i], tree)))

# Check an invalid proof
print("\n(invalid proof) check tree[0][1] = " + "001")
assert(not(verify_proof("001",root,compute_proof("000", tree))))
