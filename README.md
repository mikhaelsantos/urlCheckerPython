urlCheckerPython
================


###What is it?


 It is an application that reads a list of URLs from a configuration file and returns information related with:

   + Status Code

   + Content Validation

   + Time to complete request
   
Is was created for me to play around with Python. And yes I am a java developer so my python is still very Java-like

###What it does?


   + Reads a list of web pages (HTTP URLs) and corresponding page content requirements from a configuration file.

   + Periodically makes an HTTP request to each page (possibility to tune the interval via a setting in the configuration file.

   + Verifies that the page content received from the server matches the content requirements.

   + Measures the latency (time it took for the web server to complete the whole request).

   + Writes a log file that shows the progress of the periodic checks distinguishing between connection level problems (e.g. the web site is down ,  content problems or  content requirements were not fulfilled).

   + Implements a single-page HTTP server interface in the same process that shows (HTML) each monitored web site and the last checked status.

###Documentation


 All documentation needed can be found in this README and through comments in the source code.

###Installation

####Requirements

   + Python 2.7 Installed

   + httplib2

####Install

   + Extract master

###Configure

   There is an configuration file named config.conf

   For the application to run properly there must be a checking period defined, example:

     [checking_period]

     period_in_seconds = 2

   The checking period is in seconds and defines the intervals of the page requests for validation

   And at least one URL defined, example:

     [URL_NAME]

     url = http://google.com

     content = any content

   It is possible to define mutiple URLs, example:

     [URL_NAME_1]

     url = http://google.com

     content = any content

     [URL_NAME_2]

     url = http://reddit.com

     content = any content

  The port can be defined by changing the PORT value
     
  The application doesn't interpret any other configurations.

###Run
 

   + python main.py

   + Check Data

       Web server - http://localhost:8300:
       
         + Url Line is green if status code is 200 and configured content existes in pages content.
         
         + Url Line is yellow if status code is 200 and configured content doesn't exist in pages content.
         
         + Url Line is red if status code is other than 200.
         
         + The page refreshes automatically depending on the checking period
     
     Log - logs/monitor.log:
         
         + Line logged as [Info] if status code is 200. Content validation is logged with True if configured content exists in pages content and False if not.
         
         + Line logged as [Error] if status code is not 200.
 
###Stop Application
 
 The application stops by pressing ctrl+c. It then stops threading and stops the http server

 
###Design


 The application was developed with modularity in mind and using the most of the existing python libraries.

 The first step was to identify the components of the application, which were:

   + The component responsible for accessing the configuration: configuration.py

   + The component for the webPages: webPage.py

   + The component for logging: Which python already has, "logging".

   + The component for the server handler: serverHandler.py.

####main.py

   + Responsible for initializing all modules

   + Starts the server

   + Stops the server

####configuration.py

   + Loads the configuration file to memory.

   + Gets the configures period that is used as the interval between requests.

   + Gets the List of urls to check.

####webPage.py

   + Creates an instance of a web page from the url in the configuration file.

   + Starts/Terminates Verifying thread

   + Verifies the connection

   + Verifies the content

   + Calculates time of request

   + Logs results

   + Returns results on demand

####serverHandler.py

   + Defines behavior on http get

   + Generates html page

 The reason for dividing the code in logical parts was to ensure clean isolation between parts, easy maintenance and scalability.

 Dividing the code makes it easier to read and if it was necessary to add more business logic, for example, to the verfyWebPages method it would be easier to change the code without impacting the rest of the application.

###Contacts

    + mikhaelsantos@gmail.com
