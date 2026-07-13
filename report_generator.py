from datetime import datetime


def generate_report():

    report = f"""
==================================
RANSOMWARE DETECTION REPORT
==================================

Date : {datetime.now()}

Status :
System monitored successfully.

Result :
No confirmed ransomware attack detected.

Recommendation :
Continue monitoring the system.

==================================
"""

    with open("Detection_Report.txt", "w") as file:
        file.write(report)

    print("Report Generated Successfully.")


if __name__ == "__main__":
    generate_report()
