## Fun proj

This will run on raspberry pi in the apartment. Goal is to collect consistent data on "things" and then do "stuff" with it.

- is my ISP providing their promised service?
- how much does the temperature in my apartment vary during the day?
- what's affecting the quality of my sleep?

### Check-off when complete (and notes when otherwise)

- [x] proto-Docker installation
- [x] run on Raspberry Pi
- [ ] figure out how to get this stupid scheduling thing to work -> why is my cronjob failing to run?????
    `*/1 * * * * /usr/bin/python3 /home/pi/Desktop/projects/home_monitor/home_monitoring/home_monitor/pipeline/loader.py`
- [x] add basic flask front end to run speed test charts
- [ ] add error handling to loader runs 
- [ ] fix how paths are used - dynamically get

### Next logging to add
- [ ] environmental monitor (temp, humidity, lux) attached to rasbpi
- [ ] sleep influences google sheets

#### Notes

- for now, backup the database on GitHub


----
#### Issues
- [] favicon not loading on swebsites for some reason
- [] scheduled recurring script run with `watch -n150 python3 pipeline/loader.py` because can't get `cron` or `at` to work 