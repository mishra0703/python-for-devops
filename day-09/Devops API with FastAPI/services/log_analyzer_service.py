import os


def read_logs():
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    log_path = os.path.join(base_dir, "..", "app.log")     
    
    with open(log_path, "r") as log_file:
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


def summary():
    
    logs_count = count_logs()

    if logs_count['ERROR'] > 15:
        logs_count.update({"Suggestion" : "!! Debug your code now !!"})
    elif logs_count['WARNING'] > 10:
        logs_count.update({"Suggestion" : "You need to review your code"})        
    else:
        logs_count.update({"Suggestion" : "Don't touch your code , It is working fine"})

    return logs_count

