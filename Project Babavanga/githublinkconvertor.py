def convert_github_blob_to_raw(links):
    """
    Convert GitHub 'blob' URLs to 'raw.githubusercontent' URLs.
    Leaves links unchanged if they are already raw or do not match the expected pattern.
    """
    raw_links = []
    for link in links:
        if "github.com" in link and "/blob/" in link:
            raw_link = link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            raw_links.append(raw_link)
        else:
            raw_links.append(link)
    return raw_links


def print_links_in_asset_style(links, indent=6, trailing_comma=True, wrap_array=False):
    """
    Print links in the style:
          "https://example.com/image1.png",
          "https://example.com/image2.png",
    Parameters:
        indent (int): number of spaces before each line.
        trailing_comma (bool): whether to keep a comma after the last item.
        wrap_array (bool): if True, wrap output with [ and ] to form an array.
    """
    converted = convert_github_blob_to_raw(links)
    space = " " * indent

    if wrap_array:
        print("[")  # Uncomment wrap_array=True when calling to include brackets.

    last_index = len(converted) - 1
    for i, url in enumerate(converted):
        is_last = (i == last_index)
        if trailing_comma:
            # Always put a comma (style you showed)
            print(f'{space}"{url}",')
        else:
            # Omit comma on the last item if not trailing_comma
            comma = "," if not is_last else ""
            print(f'{space}"{url}"{comma}')

    if wrap_array:
        print("]")


# Example input links
links = [
    "https://github.com/Sivatech24/ImgHost/blob/2bc93254b2371f70aa38d0ba61d8d720ea223631/ImagesSet2/A%20new%20race%20of%20humans%20emerges/a_new_race_of_humans_emerges_4karww6ljodp1tn8078e_0.png",
    "https://github.com/Sivatech24/ImgHost/blob/2bc93254b2371f70aa38d0ba61d8d720ea223631/ImagesSet2/A%20new%20race%20of%20humans%20emerges/a_new_race_of_humans_emerges_1zsl12hsmdbh25lc4xtv_2.png",
    "https://github.com/Sivatech24/ImgHost/blob/90a544b39117e8bb5e0c9fc8f0c6ed86b2d67e0e/ImagesSet3/The%20world%20ends/Leonardo_Kino_XL_The_world_ends_2.jpg",
    "https://github.com/Sivatech24/ImgHost/blob/90a544b39117e8bb5e0c9fc8f0c6ed86b2d67e0e/ImagesSet3/The%20world%20ends/Leonardo_Kino_XL_The_world_ends_3.jpg"
]

# Print in the requested style (trailing commas like your example)
print_links_in_asset_style(links, indent=6, trailing_comma=True, wrap_array=False)

# If you later want a valid JavaScript array without trailing comma:
# print_links_in_asset_style(links, indent=2, trailing_comma=False, wrap_array=True)
