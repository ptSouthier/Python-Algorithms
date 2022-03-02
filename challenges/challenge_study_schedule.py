def check_entry(entry):
    if entry is None:
        return None


def study_schedule(permanence_period, target_time):
    students_present = 0

    check_entry(target_time)

    for student in permanence_period:
        try:
            if student[0] <= target_time <= student[1]:
                students_present += 1
        except TypeError:
            return None

    return students_present
