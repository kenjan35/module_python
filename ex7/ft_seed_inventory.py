def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None :
    units = ["packets", "grams", "area"]
    seed = seed_type.capitalize() + " seeds:"
    if unit not in units:
        print(f"{seed}Unknown unit type")
        return
    if unit == units[0]:
        print(f"{seed} {quantity} packets available")
    elif unit == units[1]:
        print(f"{seed} {quantity} grams total")
    else:
        print(f"{seed} covers {quantity} square meters")