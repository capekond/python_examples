import multiprocessing
import threading
import time
import subprocess

def publish_log(log_file: str, process_name: str):
    first_line_reported  = 1
    while True:
        time.sleep(0.5)
        p0 = subprocess.Popen(f"wc -l {log_file}" + "|awk  '{print $1}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p0.communicate()
        line_count = int(output.decode('utf-8'))
        p0 = subprocess.Popen(f"awk 'NR >= {first_line_reported} && NR <= {line_count}' {log_file}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p0.communicate()
        lines = output.decode('utf-8')
        for ln in lines.splitlines():
            print(f"{process_name} :: {ln}")
        first_line_reported = line_count + 1
def logging_sim(log_file: str):
    i = 1
    subprocess.Popen(f"echo 'Line number {i}' > {log_file}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        i += 1
        time.sleep(0.1)
        subprocess.Popen(f"echo 'Line number {i}' >> {log_file}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



if __name__ =="__main__":
    FILE = "/tmp/simulation.log"
    log_sim = multiprocessing.Process(target=logging_sim, args=(FILE,))
    log_pub = multiprocessing.Process(target=publish_log, args=(FILE,"logging file"))
    log_sim.start()
    log_pub.start()
    time.sleep(5)
    log_sim.terminate()
    time.sleep(1)
    log_pub.terminate()





