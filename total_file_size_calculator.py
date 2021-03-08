import os

total_size = 0

for i in os.listdir('C:\\exampledir'):
    if os.path.isfile(os.path.join('C:\\exampledir', i)):
        total_size += os.path.getsize(os.path.join('C:\\exampledir', i))

print(total_size)