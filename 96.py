dict1 = {
    'name': 'Divya',
    'id': 49,
    'gender': 'female',
    'age': 24,
    'likes': 34

}

dict2 = {
    'name': 'Kalyan',
    'id': 34,
    'gender': 'male',
    'age': 25,
    'likes': 49
}

result = {**dict1, **dict2}
print(result)