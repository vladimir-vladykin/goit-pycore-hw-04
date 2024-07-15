from pathlib import Path


def visualize_dir(path: str):
    directory = Path(path)

    if not directory.is_dir():
        print(f"{path} is not a dir, we cannot visualize it")
        return
    
    render_dir(directory)
    

def render_dir(directory: Path, depth_level: int = 0):
    render_item(directory.name, depth_level)
    for dir_item in directory.iterdir():
        if dir_item.is_file():
            render_item(dir_item.name, depth_level + 1)
        if dir_item.is_dir():
            render_dir(dir_item, depth_level + 1)

def render_item(item_name: str, depth_level: int):
    # TODO are dots OK considering there's hidden files?
    prefix = "" if depth_level == 0 else "." * (depth_level * 4)
    print(f"{prefix}{item_name}")


if __name__ == "__main__":
    # TODO rename to main, and parse args inside?
    visualize_dir("")