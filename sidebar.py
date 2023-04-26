# coding=utf-8
import os

rootdir = "./wiki"

for subdir, dirs, files in sorted(os.walk(rootdir)):
    dirs = sorted(dirs)
    files = sorted(files)
    if subdir == rootdir or '草稿' in subdir:
        continue

    # wiki下只有一層的資料夾
    if not dirs:
        f = open(subdir + "/_sidebar.md", "w")
        f.write("* [< Home](/)\n")
        # README => 標題
        path = subdir.replace(".", "") + "/"
        title = subdir.split("/")[-1]
        if ']' in title:
            title = title.split(']')[-1]
        f.write("* [{}]({})\n".format(title, path))

        for file in files:
            if ".md" in file:
                name = file.split(".md")[0]
                file = file.replace(" ", "%20")
                if name == "_sidebar":
                    continue
                if name == "README":
                    continue
                else:
                    path = subdir.replace(".", "") + "/" + name
                    if ']' in name:
                        name = name.split(']')[-1]
                    
                    f.write("  * [{}]({})\n".format(name, path))
        f.close()


root_file = open('_sidebar.md', "w")
root_file.write("* [Home](/)\n")
for subdir, dirs, files in sorted(os.walk(rootdir)):
    # dirs = sorted(dirs)
    # files = sorted(files)
    
    
    if subdir == rootdir or '草稿' in subdir:
        continue
    # wiki下只有一層的資料夾
    if not dirs:
        path = subdir + "/_sidebar.md"
        with open(path) as f:
            for line in f.readlines():
                if 'Home' in line: continue
                line = line.replace(' ', '%20')
                root_file.write(line)
                
root_file.close()