import random


RECOMMENDATIONS = [
    'Хвалю!', 'Молодец!', 'Отличная работа!', 'Справился лучше всех!'
]

def fix_marks(name):
    schoolkid = get_schoolkid(name)
    Mark.objects.filter(schoolkid=schoolkid.id, points__in=[2,3]).update(points=5)


def remove_chastisements(schoolkid):
    schoolkid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid.id)
    schoolkid_chastisements.delete()


def get_schoolkid(name):   
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return schoolkid
    except (Schoolkid.DoesNotExist, Schoolkid.MultipleObjectsReturned) as ex:
        raise ex



def get_subject(subject, schoolkid):
    try:
        subject = Subject.objects.get(title=subject, year_of_study=schoolkid.year_of_study)
        return subject
    except (Subject.DoesNotExist, Subject.MultipleObjectsReturned) as ex:
        raise ex


def create_commendation(name, subject):
    schoolkid = get_schoolkid(name)
    subject = get_subject(subject, schoolkid)
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter, 
        subject=subject.id).order_by("-date").first()
    
    if lesson:
        commendation = Commendation.objects.create(
            text=random.choice(RECOMMENDATIONS),
            created=lesson.date, 
            schoolkid=schoolkid, 
            subject=subject, 
            teacher=lesson.teacher
            )
        

    
