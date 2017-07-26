def show_by_percent(num, per_list):
    num_percent = num * 100
    total = 0
    for i in per_list:
        total = total + i[1]
        if num <= total:
            return i[0]
