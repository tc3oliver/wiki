import os

def create_readme_if_not_exists(path):
    """
    如果指定路徑下沒有 README.md，就建立一個，標題為資料夾名稱

    :param path: 字串，指定路徑
    """
    # 取得資料夾名稱
    folder_name = os.path.basename(path)
    # 檢查路徑下是否已經存在 README.md
    if os.path.exists(os.path.join(path, 'README.md')):
        print('README.md already exists')
    else:
        # 如果不存在，建立 README.md
        with open(os.path.join(path, 'README.md'), 'w') as f:
            # 寫入標題
            if ']' in folder_name:
                folder_name = folder_name.split(']')[-1]
            f.write(f'# {folder_name}')
            print('README.md created')

def get_parent_path(path):
    # 拆分路徑字串為一個列表
    path_list = path.split("/")
    # 如果路徑最後一個元素是空字串，則刪除它
    if path_list[-1] == "":
        path_list.pop()
    # 如果路徑只有一級，即為根路徑，則返回根路徑
    if len(path_list) == 1:
        return path_list[0]
    # 否則刪除列表中的最後一個元素，即當前路徑的最後一級
    path_list.pop()
    # 將剩下的路徑列表重新組合成字串
    parent_path = "/".join(path_list)
    return parent_path


def create_sidebar(path):
    print(path)
    # 如果指定路徑下沒有 README.md，就建立一個，標題為資料夾名稱
    create_readme_if_not_exists(path)
    # 讀取目錄
    dirs = os.listdir(path)
    # 篩選出資料夾和檔案
    dirs = [d for d in dirs if os.path.isdir(
        os.path.join(path, d)) or d.endswith(".md")]
    
    # 排序資料夾和檔案
    dirs.sort()
    dirs.sort(key=lambda x: ( x.endswith('.md'), x))

    # 設定 _sidebar.md 的檔案路徑
    sidebar_path = os.path.join(path, "_sidebar.md")
    # 清空 _sidebar.md 的內容
    with open(sidebar_path, "w") as f:
        f.write("")
        # 寫第一行返回鍵
        pp = get_parent_path(path).replace("./", "/")

        if pp == '/wiki':
            pp = '/'

            n = path.split('/')[-1]
            if ']' in n:
                n = n.split(']')[-1]
            f.write(f"* [⬅︎]({pp})\n")
            f.write(f"* [{n}]({path+'/'})\n")

        else:
            pp += '/'
            f.write(f"* [⬅︎]({pp})\n")
        

    # 處理每個資料夾和檔案
    for d in dirs:
        # 資料夾的路徑
        dir_path = os.path.join(path, d)
        # 如果是資料夾，遞迴處理
        if os.path.isdir(dir_path):
            # 設定資料夾的名稱和路徑
            dir_name = os.path.basename(dir_path)
            dir_link = os.path.join(path, dir_name)
            dir_link = dir_link.replace("./", "/")
            # 在 _sidebar.md 中添加資料夾的連結
            with open(sidebar_path, "a") as f:
                f.write(f"  * [📁 {dir_name}]({dir_link}/)\n")
            # 遞迴處理資料夾
            create_sidebar(dir_path)
        # 如果是檔案，處理 .md 檔案
        elif d.endswith(".md"):
            # 設定檔案的名稱和路徑
            file_name = d[:-3]
            file_link = os.path.join(path, d)

            file_link = file_link.split(".md")[0]
            file_link = file_link.replace("./", "/")
            file_link = file_link.replace(' ', '%20')

            # 過濾 _sidebar 及 README
            if file_name == "_sidebar":
                continue
            if file_name == "README":
                continue
            if ']' in file_name:
                file_name = file_name.split(']')[-1]

            # 在 _sidebar.md 中添加檔案的連結
            with open(sidebar_path, "a") as f:
                f.write(f"  * [📄 {file_name}]({file_link})\n")


# create_sidebar("./wiki/[B]Cryptography")
# create_sidebar("./wiki/[C]Flutter")

rootdir = './wiki'

root_file = open('_sidebar.md', "w")
root_file.write("* [Home](/)\n")

list = []
for subdir, dirs, files in os.walk(rootdir, topdown=True):
    if subdir != rootdir: dirs.clear()  # 遍歷子目錄時，清空子目錄列表，防止遞迴深入
    if not dirs: list.append((subdir, dirs, files))

for subdir, _, _ in sorted(list):

    if subdir == rootdir or '草稿' in subdir:
        continue
    
    create_sidebar(subdir)

    path = subdir + "/_sidebar.md"

    with open(path) as f:
            for line in f.readlines():
                if '⬅︎' in line: continue
                root_file.write(line)

root_file.close()
