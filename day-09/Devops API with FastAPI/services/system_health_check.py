import psutil

def check_system_health():

    threshold_values = [45,80,50]

    curr_cpu_threshold = psutil.cpu_percent(interval=1)
    curr_memory_threshold = psutil.virtual_memory().percent
    curr_disk_threshold = psutil.disk_usage('/').percent


    disk_state = "Disk is almost full" if curr_disk_threshold > threshold_values[2] else "You still have some disk space left"


    memory_state = "Memory is about to get full" if curr_memory_threshold > threshold_values[1] else "You still have enough memory"


    cpu_state = "CPU is at high risk" if curr_cpu_threshold > threshold_values[0] else "CPU is working fine"

    return {
        "cpu_percentage": curr_cpu_threshold,
        "CPU_status": cpu_state,
        "disk_percentage": curr_disk_threshold,
        "Disk_status": disk_state, 
        "memory_percentage": curr_memory_threshold,        
        "Memory_status": memory_state
    }


