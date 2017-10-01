import os
directory = 'D:\KwDownload'
for filename in os.listdir(directory):
    if filename.find('(1)') !=-1 or filename.find('(2)')!=-1 or filename.find('(3)')!=-1:
        # print(os.path.join(directory, filename))
        os.remove(os.path.join(directory, filename))
        continue
    else:
        continue