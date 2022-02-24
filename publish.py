print('Publsh!')

import os

target = '_notes/Public'
notes_in_target = os.listdir(target)

for note in notes_in_target:
    f = open(target + '/' + note, 'r')
    lines = f.readlines()
    isPublic = False
    for line in lines:
        if '#Torvalz' in line:
            isPublic = True
            print(line)
            break
    # unlink
    if isPublic == False:
        command = 'rm "' + target + '/' + note + '"'
        os.system(command)
        print('Delete: ' + note)

source = os.path.expanduser('~') + '/Vault/notes'
notes_in_source = os.listdir(source)

for note in notes_in_source:
    f = open(source + '/' + note, 'r')
    lines = f.readlines()
    for line in lines:
        if '#Torvalz' in line:
            command = 'ln "' + source + '/' + note + '" "' + target + '/' + note + '"'
            print('Publish: ', note)
            os.system(command)
            break

os.system('./push.sh')