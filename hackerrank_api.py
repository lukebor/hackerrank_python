import os
with open('borecki_lukasz_data.json') as file:

    data=eval(file.read())
    for sub in data['submissions']:
        #print(sub['challenge'])


        if not os.path.exists(sub['challenge']) and sub['language']=='python3':
            os.makedirs(sub['challenge'])
