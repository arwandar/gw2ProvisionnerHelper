def formatPrice(price):
    price = price.__str__().rjust(6, "0")
    pc = int(price[-2:])
    ps = int(price[-4:-2])
    po = int(price[0:-4])
    return "{po}po {ps}ps {pc}pc".format(po=po, ps=ps, pc=pc)
