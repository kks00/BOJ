from input_from_file import init_file, input
init_file("1991")

root = {
    "key": "A",
    "Left": None,
    "Right": None
}

def insert(root, p, l, r):
    if root is None:
        return False
    if root["key"] == p:
        if l is not None:
            root["Left"] = {"key": l, "Left": None, "Right": None}
        if r is not None:
            root["Right"] = {"key": r, "Left": None, "Right": None}
        return True
    if insert(root["Left"], p, l, r):
        return True
    if insert(root["Right"], p, l, r):
        return True
    return False

N = int(input().rstrip())
for _ in range(N):
    p, l, r = input().rstrip().split()
    l = l if l != "." else None
    r = r if r != "." else None
    insert(root, p, l, r)

# print(root)

def traverse(root, order):
    if root is None:
        return
    if order == "pre":
        print(root["key"], end="")
    traverse(root["Left"], order)
    if order == "mid":
        print(root["key"], end="")
    traverse(root["Right"], order)
    if order == "post":
        print(root["key"], end="")

traverse(root, "pre")
print()
traverse(root, "mid")
print()
traverse(root, "post")
print()