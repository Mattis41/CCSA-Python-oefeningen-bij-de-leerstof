def zoekBinair(zoekItem, rij):
    l = 0
    r = len(rij) - 1

    while l != r:
        m = (l + r) // 2
        print(f"{l}, {r}")
        if rij[m] < zoekItem:
            l = m + 1
        else:
            r = m
            
    # Vanaf hier ben je uit de while-lus.
    if rij[l] == zoekItem:
        index = l
    else:
        index = -1
        
    return index

# De aanroep moet exact dezelfde naam hebben als de definitie
print("index = ", zoekBinair(70, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]))