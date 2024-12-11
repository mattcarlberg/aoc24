import sys

def safe_report(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    all_pos = all([a > 0 for a in diffs])
    if(all_pos and max(diffs) <= 3):
        return True
    all_neg = all([a < 0 for a in diffs])
    if(all_neg and min(diffs) >= -3):
        return True
    return False 


vals = []

vals = [line.strip().split() for line in sys.stdin]


count = 0 
for report in vals:
    report = [int(a) for a in report]


    
    if(safe_report(report)):
        count+=1
    

    
print(count)