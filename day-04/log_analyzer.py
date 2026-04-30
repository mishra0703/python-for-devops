def read_logs():
    with open("app.log","r") as log_file:
        return log_file.readlines()


def count_logs():
    log_count = {"INFO" : 0 , "WARNING" : 0 , "ERROR" : 0}
    logs = read_logs()

    for line in logs:
        if "INFO" in line:
            log_count["INFO"]+=1
        if "WARNING" in line:
            log_count["WARNING"]+=1
        if "ERROR" in line:
            log_count["ERROR"]+=1

    return log_count    


def summary_file(logs):

    report = []

    report.append("\n----- Summary Report -----\n")

    report.append("| State    | Count |\n")
    report.append(f"  Info        {logs['INFO']}\n")
    report.append(f"  Warning     {logs['WARNING']}\n")
    report.append(f"  Errors      {logs['ERROR']}\n")   


    if logs['ERROR'] > 15:
        report.append("\n\n----- SUGGESTIONS -----\n")
        report.append("!! Debug your code now !!\n")
    elif logs['WARNING'] > 10:
        report.append("\n\n----- SUGGESTIONS -----\n")
        report.append("You need to review your code\n")

    return "".join(report)


Summary_Report = summary_file(count_logs())
print(Summary_Report)                       # Output in Terminal


with open("log_summary.txt","w") as log_report:
    log_report.write(Summary_Report)        # Output in .txt File