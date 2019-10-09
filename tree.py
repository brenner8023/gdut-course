# 递归遍历获取所有文件, 目录文件的结构如下:
# [
#     {
#         name: "大一",
#         children: [{}, {}]
#     },
#     {
#         name: abc.md,
#         children: null
#     }
# ]

import os, time, json

def getPath(target):
    fileTree = []
    dirs_arr = []
    files_arr = []

    for name in os.listdir(target):
        if (name != '.git') and (name != 'tree.py') and (name != 'README.md') and (name != 'db.js'):
            curr = target + '/' + name
            # 判断是文件还是文件夹
            if os.path.isdir(curr):
                dirs_arr.append(name)
            elif os.path.isfile(curr):
                files_arr.append(name)
    # 遍历当前所有同级文件夹
    for i in range(len(dirs_arr)):
        next = os.path.join(target, dirs_arr[i])

        mtime = time.localtime(os.stat(next).st_mtime)
        mtime_str = ''.join([str(mtime[0]), '年', str(mtime[1]), '月', str(mtime[2]), '日'])

        fileTree.append({
            'name': dirs_arr[i],
            'mtime': mtime_str,
            'children': getPath(next)
        })

    # 遍历当前所有同级文件
    for i in range(len(files_arr)):
        next = os.path.join(target, files_arr[i])

        mtime = time.localtime(os.stat(next).st_mtime)
        mtime_str = ''.join([str(mtime[0]), '年', str(mtime[1]), '月', str(mtime[2]), '日'])

        fileTree.append({
            'name': files_arr[i],
            'mtime': mtime_str,
            'url': ''.join(['https://github.com/brenner8023/gdut-course/tree/master/', next]),
            'children': 'null'
        })

    return fileTree

def main():
    template = 'const fileTree = '
    template += json.dumps(getPath('.'))
    template += """;

export default fileTree;"""
    
    with open('./db.js', 'w+') as f:
        f.write(template)

if __name__ == "__main__":
    main()