def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None :
    units = ["packets", "grams", "area"]
    print(f"{seed_type.capitalize()} seeds: ")
    if unit not in units:
        print("Unknown unit type")
        return
    if unit == units[0]:
        print(f"{quantity} packets available")
    elif unit == units[1]:
        print(f"{quantity} grams total")
    else:
        print(f"covers {quantity} square meters")