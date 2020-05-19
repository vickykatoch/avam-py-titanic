
def get_title(name):
    title_group = {'mr': 'Mr',
                   'mrs': 'Mrs',
                   'miss': 'Miss',
                   'master': 'Master',
                   'don': 'Sir',
                   'rev': 'Sir',
                   'dr': 'Officer',
                   'mme': 'Mrs',
                   'ms': 'Mrs',
                   'major': 'Officer',
                   'lady': 'Lady',
                   'sir': 'Sir',
                   'mlle': 'Miss',
                   'col': 'Officer',
                   'capt': 'Officer',
                   'the countess': 'Lady',
                   'jonkheer': 'Sir',
                   'dona': 'Lady'
                   }
    first_name = name.split(',')[1]
    title = first_name.split('.')[0]
    title = title.strip().lower()
    return title_group[title]
