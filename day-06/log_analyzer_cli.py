import argparse



class LogAnalyzer:

    def __init__(self,log_file,output_filename):        
        self.log_file = log_file        
        self.output_file = output_filename


    def read_logs(self):
        with open(self.log_file,"r") as log_file_lines:
            return log_file_lines.readlines()



    def count_logs(self):
        log_count = {"INFO" : 0 , "WARNING" : 0 , "ERROR" : 0}
        logs = self.read_logs()

        for line in logs:
            if "INFO" in line:
                log_count["INFO"]+=1
            if "WARNING" in line:
                log_count["WARNING"]+=1
            if "ERROR" in line:
                log_count["ERROR"]+=1

        return log_count    



    def summary_file(self,logs):

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

        
        with open(self.output_file,"w") as log_report:
            log_report.write("".join(report))            # Output in .txt File

        return "".join(report)




def main():

    parser = argparse.ArgumentParser(description="To pass input and output filepath")

    parser.add_argument("--file", required=True , help="Input file path")
    parser.add_argument("--out", required=True , help="Output file path")

    args = parser.parse_args()    

    logs_report = LogAnalyzer(args.file,args.out)
    log_lines = logs_report.count_logs()

    Summary_Report = logs_report.summary_file(log_lines)
    print(Summary_Report)       # Output in Terminal




if __name__ == "__main__":
    main()
