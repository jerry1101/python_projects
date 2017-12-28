# Project: python_server_monitoring

One Paragraph of project description goes here

## Compare configuration files and log changes

### Related Files:

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Install Steps:

What things you need to install the software and how to install them
      1. Give execute permission to that script using
          chmod a+x foo.py
      
      1. Enter crontab editor
      crontab -e
      
      1. Setup cron expression:
      50 19 * * * python hello.py 
      command to execute define the time of execution of the job. The timing syntax has five parts:
```
minute
hour
day of month
month
day of week
```
```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds
