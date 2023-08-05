from datacenter.models import (
    Schoolkid,
    Lesson, 
    Mark, 
    Commendation, 
    Subject, 
    Chastisement)


def fix_marks(schoolkid):
    schoolkid_bad_marks = Mark.objects.filter(schoolkid=schoolkid.id, points__in=[2,3])
    for mark in schoolkid_bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    schoolkid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid.id)
    schoolkid_chastisements.delete()


def create_commendation(name, subject):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
    except Exception as ex:
        print("Укажите имя и фамилию или полное ФИО")
    subject = Subject.objects.get(title=lesson, year_of_study=schoolkid.year_of_study)
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter, 
        subject=subject.id).first()
    ivan_comment = Commendation(
        text="Хвалю!",
        created=lesson.date, 
        schoolkid=schoolkid, 
        subject=subject, 
        teacher=lesson.teacher
        )
    ivan_comment.save()