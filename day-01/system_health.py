import psutil

def threshold_inputs():
    cpu_threshold = int(input("Enter CPU Threshold Value : "))
    memory_threshold = int(input("Enter Memory Threshold Value : "))
    disk_threshold = int(input("Enter Disk Threshold Value: "))

    thresholds_value = [cpu_threshold , memory_threshold , disk_threshold]
    return thresholds_value



def system_health_check(threshold_values):
    curr_cpu_threshold = psutil.cpu_percent(interval=1)
    curr_memory_threshold = psutil.virtual_memory()
    curr_disk_threshold = psutil.disk_usage('/')

    print(f"\n------ Disk usage (in %) ------\n{curr_disk_threshold.percent}\n")

    if curr_disk_threshold.percent > threshold_values[2] :
        print("WARNING ! WARNING ! WARNING !")
        print("----- Disk Usage is at peak ------")
    else:
        print("Your Disk is fine <3")


    print(f"\n------ Memory Usage (in %) ------\n{curr_memory_threshold.percent}\n")

    if curr_memory_threshold.percent > threshold_values[1] :
        print("WARNING ! WARNING ! WARNING !")
        print("----- Memory Usage is at peak ------")
    else:
        print("Your Memory is fine <3")


    print(f"\n------ CPU Usage ------\n{curr_cpu_threshold}\n")

    if curr_cpu_threshold > threshold_values[0] :
        print("WARNING ! WARNING ! WARNING !")
        print("----- CPU Usage is at peak ------")
    else:
        print("Your CPU is fine <3")




system_threshold_values = threshold_inputs()
system_health_check(system_threshold_values)

