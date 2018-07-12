import numpy as np
import csv
import pdb

head = ["engine", "month", "air_temp", "noise", "egt", "ff", "n1", "n2", "fp_noise", "fp_egt", "fp_ff", "fp_n1", "fp_n2", "failure_prob"]                
body = {}
prev_egt = 0
prev_ff = 0
prev_n1 = 0
prev_n2 = 0

with open("../../data/mlr_final_data.csv", "w") as csv_file :
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerows([head])
    
    for engine_no in range(1, 2):
    
        body[engine_no] = {}
        
        for month in range(1, 61):
            
            body_w = []
            
            body[engine_no][month] = {}
            
            body[engine_no][month]['air_temp'] = np.random.randint(-15, 1)
            
            body[engine_no][month]['fp_noise'] = 0
            body[engine_no][month]['fp_egt'] = 0
            body[engine_no][month]['fp_ff'] = 0
            body[engine_no][month]['fp_n1'] = 0
            body[engine_no][month]['fp_n2'] = 0
            body[engine_no][month]['failure_prob'] = 0
                            
            if month == 1:
                
                body[engine_no][month]['noise'] = 130
                body[engine_no][month]['egt'] = 1300
                body[engine_no][month]['ff'] = 5000
                body[engine_no][month]['n1'] = 12000
                body[engine_no][month]['n2'] = 10000
                
            else:
                
                prev_noise = body[engine_no][month-1]['noise']
                prev_egt = body[engine_no][month-1]['egt']
                prev_ff = body[engine_no][month-1]['ff']
                prev_n1 = body[engine_no][month-1]['n1']
                prev_n2 = body[engine_no][month-1]['n2']
                
                body[engine_no][month]['noise'] = round(prev_noise + np.random.uniform(0.15, 0.8), 2)
                body[engine_no][month]['egt'] = prev_egt + np.random.randint(40, 45)
                body[engine_no][month]['ff'] = prev_ff + np.random.randint(37, 42)
                body[engine_no][month]['n1'] = prev_n1 + np.random.randint(99, 106)
                body[engine_no][month]['n2'] = prev_n2 + np.random.randint(102, 106)

            body_w.append(str(engine_no))
            body_w.append(str(month))
            body_w.append(str(body[engine_no][month]['air_temp']))
            body_w.append(str(body[engine_no][month]['noise']))
            body_w.append(str(body[engine_no][month]['egt']))
            body_w.append(str(body[engine_no][month]['ff']))
            body_w.append(str(body[engine_no][month]['n1']))
            body_w.append(str(body[engine_no][month]['n2']))
            body_w.append(str(body[engine_no][month]['fp_noise']))
            body_w.append(str(body[engine_no][month]['fp_egt']))
            body_w.append(str(body[engine_no][month]['fp_ff']))
            body_w.append(str(body[engine_no][month]['fp_n1']))
            body_w.append(str(body[engine_no][month]['fp_n2']))
            body_w.append(str(body[engine_no][month]['failure_prob']))            
            
            writer.writerows([body_w])
            