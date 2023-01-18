from shutil import copyfile
import pickle
copyfile('student_info.pkl', 'updated_info.pkl')

def add_student_info(new_student):
    with open('student_info.pkl', 'rb') as f:
        student_info = pickle.load(f)

    for idx, person in enumerate(student_info):
        if person['id'] == new_student['id']:
            target = idx
            break

    student_info[target].update(new_student)

    with open('updated_info.pkl', 'wb') as f:
        pickle.dump(student_info,f)
new_student = {
        'id': 20200000,
        'name': 'Nguyen Van Anh',
        'score': {
            'math': 7.8,
            'english': 8.4,
            'physics': 8.0,
        }
    }
add_student_info(new_student)