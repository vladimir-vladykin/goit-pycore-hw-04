from pathlib import Path
from colorama import Fore, Back, Style

colors_pallete = (Fore.CYAN, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.YELLOW)
depth_step = 4
depth_indicator = "~"

def visualize_dir(path: str):
    directory = Path(path)

    if not directory.is_dir():
        print(f"{path} is not a dir, we cannot visualize it")
        return
    
    # adjust background and style once here.
    # text color will be adjusted dynamically for each item
    print(Back.WHITE)   
    print(Style.BRIGHT)

    render_dir(directory)
    

def render_dir(directory: Path, depth_level: int = 0):
    render_item(directory.name, depth_level)

    # iterate through all directly and render all we found
    for dir_item in directory.iterdir():
        if dir_item.is_file():
            render_item(dir_item.name, depth_level + 1)
        if dir_item.is_dir():
            render_dir(dir_item, depth_level + 1)

def render_item(item_name: str, depth_level: int):
    # select text color based on current depth
    adjust_text_color(depth_level)
    
    # format prefix to better visualize depth of item
    prefix = "" if depth_level == 0 else depth_indicator * (depth_level * depth_step)

    print(f"{prefix}{item_name}")

def adjust_text_color(depth_level):
    print(colors_pallete[depth_level % len(colors_pallete)])


if __name__ == "__main__":
    # TODO rename to main, and parse args inside?
    # visualize_dir("/Users/volodymyr_vl/reports_sent")
    visualize_dir(".")