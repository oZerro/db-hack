import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


recommendations = [
    'Хвалю!', 'Молодец!', 'Отличная работа!', 'Справился лучше всех!'
]

def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid.id, points__in=[2,3]).update(points=5)


def remove_chastisements(schoolkid):
    schoolkid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid.id)
    schoolkid_chastisements.delete()


def create_commendation(name, subject):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except (ObjectDoesNotExist, MultipleObjectsReturned) as ex:
        print("Укажите имя и фамилию или полное ФИО")
        
    subject = Subject.objects.get(title=subject, year_of_study=schoolkid.year_of_study)
    
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter, 
        subject=subject.id).first()
    
    if lesson:
        ivan_recommendation = Commendation.objects.create(
            text=random.choice(recommendations),
            created=lesson.date, 
            schoolkid=schoolkid, 
            subject=subject, 
            teacher=lesson.teacher
            )
        

    