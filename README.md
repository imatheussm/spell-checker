<p align="center"><img src="./igor-matheus.png"></img></p>

# `spell-checker`

**Python-made, object-oriented, tree-based spell-checking tools** 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/imatheussm/spell-checker/master?filepath=spell_checker.ipynb)

## N-ary Trees

According to [Wikipedia](https://en.wikipedia.org/wiki/M-ary_tree), a **N-ary Tree** (or **M-ary**, as they put it) is nothing more than "a rooted tree in which each node has no more than m children". Binary and ternary trees are special cases of this kind of tree, where `m = 2` and `m = 3`, respectively.

N-Ary Trees are a type of data structure and are studied along with graphs, lists, stacks, heaps, queues and so on.

More can be read in the Wikipedia page mentioned above.

### Trie Trees

According to [Wikipedia](https://en.wikipedia.org/wiki/Trie), a **Trie Tree** is a kind of [search tree](https://en.wikipedia.org/wiki/Search_tree), which, by its turn, is "a tree data structure used for locating specific keys from within a set". According to Wikipedia, a Trie Tree can be also refeered to as Radix Trees or Prefix Trees – however, in the implementation seen in this repository, this is not the case: the CharacterTree class, which is a Trie Tree, only store a single character per Node, no matter what, while the RadixTree class stores radices whenever possible.

### Radix Trees

According to [Wikipedia](https://en.wikipedia.org/wiki/Radix_tree) (there's also information under [Wikipedia's Trie page](https://en.wikipedia.org/wiki/Trie)), a **Radix Tree**, or **Compact Prefix Tree**, attempts to store as much characters under each Node as possible. This is made possible by making paths trough prefixes and merging tries whenever possible.

## Project goals

- **Employ data structures:** in this case, trie and radix trees
- **Build a tool from the scratch:** in this case, a spell-checker like those present in keyboards and WYSIWYG document editors
- **Complement other data-structure-based projects:** recently, I forked a Uno implementation in Python with `pygamezero` ([@imatheussm/uno](https://github.com/imatheussm/uno), forked from [@bennuttall/uno](https://github.com/bennuttall/uno)) and changed it to use a kind of doubly-linked circular list I created. However, I found it to be too lame to just make this adaption, and instead of stopping there, I decided to go further and build something else from scratch
