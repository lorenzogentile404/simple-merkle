# simple-merkle

This script contains a simple implementation of [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree), giving the chance to the user to compute inclusion proofs and verify them.

Here is an example of the output:

```console
(base) user@host:~$ python simple_merkle.py 
tree =
['eac86...']
['5de0a...', '99d32...']
['2ac9a...', '7a3e6...', '13715...', '8a080...']
['000', '001', '010', '011']


root = eac8698ce7573da1439ecfcfcfd08996f7ad5d7460728a13f6da05b700499edc


element to be checked = 000
elements of the proof = 
tree[1][1] = 7a3e6...
tree[2][1] = 99d32...
obtained root = eac8698ce7573da1439ecfcfcfd08996f7ad5d7460728a13f6da05b700499edc
True

element to be checked = 001
elements of the proof = 
tree[1][0] = 2ac9a...
tree[2][1] = 99d32...
obtained root = eac8698ce7573da1439ecfcfcfd08996f7ad5d7460728a13f6da05b700499edc
True

element to be checked = 010
elements of the proof = 
tree[1][3] = 8a080...
tree[2][0] = 5de0a...
obtained root = eac8698ce7573da1439ecfcfcfd08996f7ad5d7460728a13f6da05b700499edc
True

element to be checked = 011
elements of the proof = 
tree[1][2] = 13715...
tree[2][0] = 5de0a...
obtained root = eac8698ce7573da1439ecfcfcfd08996f7ad5d7460728a13f6da05b700499edc
True
```
