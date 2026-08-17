def ft_harvest_total():
    harvest = 0
    for i in range(1, 3):
        harvest += int(input(f"Day {i} harvest: "))
    print(f"Total harvest: {harvest}")