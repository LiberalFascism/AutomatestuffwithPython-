import os,shutil
#os.chdir('E:\\Projects')
for foldername, subfolders, filenames in os.walk('E:\\Projects'):
    print('The current folder is ' + foldername)

    for subfolder in subfolders:
        print('SUBFOLDER of ' + foldername + ': ' + subfolder)

    for filename in filenames:
        os.chdir(foldername)
        
        print('file inside ' + foldername + ': ' + filename)
        if filename.endswith('.txt'):
            shutil.copy(filename, 'E:\\CopyFolder')
       
    print('')
