# print('My name is Arjun Krishna. \nI\'m a Self-taught Web and Graphic Designer. \nI\'m an intermediate in working with Vue.js, Node.js, Firebase, Arduino etc:\n\n')

name = 'Arjun Krishna'
designation = 'Self-taught Web and Graphic Designer'
skills = ['Vue.js', 'Node.js', 'Firebase', 'Arduino']

# print('My name is ' + name + '. \nI\'m a Self-taught ' + designation + '. \nI\'m an intermediate in working with ' + skills[0] + ', ' + skills[1] + ', ' + skills[2] + ', ' + skills[3] + '.')
# for s in skills:
#     print(s + ', ')

name_1 = input('\nEnter your Name : ')
designation_1 = input('Enter your Designation : ')
skills_1 = []
skills_1 = [item for item in input("Enter the list items : ").split()]
# print(skills_1)
print('\n\nMy name is ' + name_1 + '. \nI\'m a Self-taught ' + designation_1 + '. \nI\'m an intermediate in working with ' + skills_1[0] + ', ' + skills_1[1] + ', ' + skills_1[2] + ', ' + skills_1[3] + '.')
