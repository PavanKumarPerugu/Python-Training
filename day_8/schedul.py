import time

def task():
    print("Task executed!")
while True:
    if input("Should I do the job again?(y/n): ") == "y":
        task()
        time.sleep(10)  # wait 10 seconds
    else:
        print("Your job is stopped!!")
        break

# scheduling using schedule module
import schedule

def job():
    print("Job executed!")

# Schedule the job every 5 seconds
schedule.every(5).seconds.do(job)

# Schedule another job every day at 9:00 AM
# schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
