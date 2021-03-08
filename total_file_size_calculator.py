import os

total_size = 0

for i in os.listdir('C:\\Program Files\\7-Zip'):
    if os.path.isfile(os.path.join('C:\\Program Files\\7-Zip', i)):
        total_size += os.path.getsize(os.path.join('C:\\Program Files\\7-Zip', i))

print(total_size)