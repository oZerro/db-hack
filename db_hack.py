import random


RECOMMENDATIONS = [
    'Хвалю!', 'Молодец!', 'Отличная работа!', 'Справился лучше всех!'
]

def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid.id, points__in=[2,3]).update(points=5)


def remove_chastisements(schoolkid):
    schoolkid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid.id)
    schoolkid_chastisements.delete()


def get_schoolkid(name):
    while True:
        try:
            schoolkid = Schoolkid.objects.get(full_name__contains=name)
        except (Schoolkid.DoesNotExist, Schoolkid.MultipleObjectsReturned) as ex:
            print("Укажите имя и фамилию или полное ФИО")
        finally:
            if schoolkid:
                break

    return schoolkid


def get_subject(subject, schoolkid):
    while True:
        try:
            subject = Subject.objects.get(title=subject, year_of_study=schoolkid.year_of_study)
        except (Subject.DoesNotExist, Subject.MultipleObjectsReturned) as ex:
            print("Проверьте переданные вами данные: Название предмета, объект школьника.")
        finally:
            if subject:
                break

    return subject


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
        

    