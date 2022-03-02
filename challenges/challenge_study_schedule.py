def study_schedule(permanence_period, target_time):
    students_present = 0

    if target_time is None:
        return None

    for student in permanence_period:
        try:
            if student[0] <= target_time <= student[1]:
                students_present += 1
        except TypeError:
            return None

    return students_present
