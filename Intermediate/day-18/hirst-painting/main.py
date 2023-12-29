import colorgram

colors = colorgram.extract('image.jpg', 6)


def rgb_colors(all_colors, list_of_colors):
    for color in all_colors:
        color_rgb = color.rgb
        list_of_colors.append(tuple(color_rgb))
    return list_of_colors


list_of_color_tups = []
print(rgb_colors(colors, list_of_color_tups))
