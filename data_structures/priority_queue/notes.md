```bash
def preorder(p)
    visit p
    for each child in children(p) then
        preorder(child)
```

```bash
def postorder(p)
    for each child in children(p) then
        prostorder(child)
    visit p
```

```bash
def breadth-first(T)
    Q = Queue(root)
    p = Q.dequeue()
    visit p
    for each child in children(p) then
        Q.enqueue(child)
```

```bash
def inorder(p)
    if p has left child lc then
        inorder(lc)
    visit p
    if p has right child rc then
        inorder(rc)
```