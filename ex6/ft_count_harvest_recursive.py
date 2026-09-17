def ft_count_harvest_recursive() -> None :
    days = int(input("Days until harvest: "))
    iterator = 1
    def count_days(harvest_time, iter):
        if iter > harvest_time:
            print("Harvest time!")
            return
        else:
            print(f"Day {iter}")
        count_days(harvest_time, iter + 1)
    count_days(days, iterator)