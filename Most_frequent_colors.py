def top_color(image):
    colors = {}
    result = []
    for i in image:
        for color in i:
            if color not in colors:
                colors[color] = 1
            else:
                colors[color] += 1

    most_freq = max(colors, key=colors.get)
    highest_value = colors[most_freq]
    for key in colors:
        if colors[key] == highest_value:
            result.append(key)
    return sorted(result)
