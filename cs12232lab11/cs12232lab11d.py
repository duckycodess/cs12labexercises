from oj import Directory, File

def files_by_size(d: Directory) -> list[tuple[str, int]]:

    def collect_files(directory: Directory, path: str, files_list: list[tuple[str, int]]) -> None:
        for name, item in directory.contents.items():
            current_path = f"{path}/{name}" if path else name
            
            if isinstance(item, File):
                files_list.append((current_path, item.size))
            else:
                collect_files(item, current_path, files_list)
    
    files_list: list[tuple[str, int]] = []
    collect_files(d, '', files_list)
    
    files_list.sort(key=lambda x: (x[1], x[0]))
    return files_list