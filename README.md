# Project: python_server_monitoring

[FUNCTION#2](#FUNCTION#2)

## [FUNCTION#1] Compare configuration files and log changes
   ------------
### Related Files:

     comp1.py 
      * Copy configuration file as archive when run the program first time
      * When find discrepancy, log in history.txt

### Install Steps:

What things you need to install the software and how to install them
      
      * Copy related files to /home/hybris(or the folder you prefer)
      
      * Give execute permission to that script using
          chmod a+x foo.py
      
      * Enter crontab editor
      crontab -e
      
      * Setup cron expression:
      50 19 * * * python hello.py 
      command to execute define the time of execution of the job. The timing syntax has five parts:
```
minute
hour
day of month
month
day of week
```



### Running the tests

```
TBD
```

### Deployment

```
TBD
```


## [FUNCTION#2] Validate Links in Sitemap Page
   -----------
### Related Files:

     validatelinks.py 
      * fetch links in a web page
      * fetch http response code(>200)
## [FUNCTION#3] Collect the non-200 response in sitemap XML files

### Related Files:

     ```
     TBD
     ```
## [FUNCTION#4] Monitor of hot folder

### TO-do
1. load file names of IP
2. find run id
3. monitor the change of file number
4. report left files
### Related Files:

     ```
     TBD
     ```
