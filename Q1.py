def availableTshirt():
    NumInShop = input()
    TshirtInShop = input().split()
    NumNeeds = input()
    TshirtNeeds = input().split()

    SizeList = {}
    for i in TshirtInShop:
        if i == "M":

    if NumInShop < NumNeeds:
        return "No"
    else:
        print(TshirtInShop)
