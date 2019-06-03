<p align="center"><img src="./igor-matheus.png"></img></p>

# `spell-checker`

**Python-made, object-oriented, tree-based spell-checking tools** 


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/imatheussm/spell-checker/master?filepath=spell_checker.ipynb)

## What are N-ary Trees?

According to [Wikipedia](https://en.wikipedia.org/wiki/M-ary_tree), a N-ary Tree (or M-ary, as they put it) is nothing more than "a rooted tree in which each node has no more than m children". Binary and ternary trees are special cases of this kind of tree, where `m = 2` and `m = 3`, respectively.

N-Ary Trees are a type of data structure and are studied along with graphs, lists, stacks, heaps, queues and so on.

More can be read in the Wikipedia page mentioned above.

## Project goals

- **Employ data structures:** in this case, n-ary trees
- **Build a tool from the scratch:** in this case, a spell-checker like those present in keyboards and WYSIWYG document editors
- **Complement other data-structure-based projects:** recently, I forked a Uno implementation in Python with `pygamezero` ([@imatheussm/uno](https://github.com/imatheussm/uno), forked from [@bennuttall/uno](https://github.com/bennuttall/uno)) and changed it to use a kind of doubly-linked circular list I created. However, I found it to be too lame to just make this adaption, and instead of stopping there, I decided to go further and build something else from scratch