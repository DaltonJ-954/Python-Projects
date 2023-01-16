import os

fname = 'css_backup.txt'

fpath = 'C:\\Users\\scall\\OneDrive\\Documents\\GitHub\\HTML-and-CSS-Projects'

Absolute = os.path.join(fpath, fname)
print(Absolute)

listsrch = os.listdir(r'C:\\Users\\scall\\OneDrive\\Documents\\GitHub\\HTML-and-CSS-Projects')
print(listsrch)
