"""gradebook.reports — build a printable report from grade records."""

from .stats import average_per_student
from .stats import subjects_offered
from .stats import top_scorer
from .stats import passing_students

def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    print("===Gradebook Report===")
    avg = average_per_student(records)
    passed = passing_students(records)
    subject = subjects_offered(records)
    topper = top_scorer(records)
    report = {
        "Total_records": len(records),
        "subjects offered": sorted(subject),
    }
    reports = {
           "top_scorrer" :topper,
          "Passing students": passed
    }
    for key,value in report.items():
        print(f'{key}: {value}')
    print("Averages: ")
    for key,value in avg.items():
        print(f'{key}: {value}')
    for key,value in reports.items():
        print(f'{key}: {value}')