import uuid
from crontab import CronTab
from datetime import datetime



class AlarmManager:
    def __init__(self):
        self.alarm_dict = {}
        self.cron = CronTab(user='root')
    def add_alarm(self,alarm):
        self.alarm_dict[alarm.id] = alarm
        job = self.cron.new(f"aplay /root/web/ringtones/{alarm.ringtone}; echo {alarm.ringtone};")
        time_format = datetime.strptime(alarm.time, "%H:%M")
        job.hour.on(int(time_format.hour))
        job.minute.on(int(time_format.minute))
        self.cron.write()
    def get_all_alarm(self):
        return self.alarm_dict.values()
    def get_alarm_by_id(self, id):
        return self.alarm_dict.get(id)

class Alarm:
    def __init__(self, name, ringtone, time):
        self.id = str(uuid.uuid4())
        self.name = name
        self.ringtone = ringtone
        self.time = time