"""gradebook.stats — aggregate statistics over grade records."""

def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    student_scores = {}

    for record in records:
        name = record["name"]
        score = record["score"]

        student_scores.setdefault(name, []).append(score)

    averages = {}

    for name, scores in student_scores.items():
        averages[name] = round(sum(scores) / len(scores), 2)

    return averages

def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    total_subjects = set()
    for students in records:
        total_subjects.add(students["subject"])
    total_subjects = sorted(total_subjects)
    return total_subjects
   
def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    avg = average_per_student(records)
    highest_name = ""
    highest_score = 0
    for name in avg:
        if avg[name] > highest_score:
            highest_name = name
            highest_score = avg[name]
    return (highest_name,highest_score)

def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    avg = average_per_student(records)
    passed = []
    for i in avg:
        if avg[i] >= threshold:
            passed.append(i)
    for i in range(len(passed)):
        for j in range(i+1,len(passed)):
            if passed[i] > passed[j]:
                temp = passed[i]
                passed[i] = passed[j]
                passed[j] = temp
    return passed