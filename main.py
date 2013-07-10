#Author: Mikhael Santos
from webPage import WebPage
from configuration import Configuration
from serverHandler import ServerHandler
import logging, shared, SocketServer,sys


"""Log configuration"""
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename= shared.LOG_PATH + '/' +shared.LOG_FILE,
                    filemode='w')                   
logger = logging.getLogger(shared.LOGGER)    

logger.info('Starting App')

"""Configuration initialization"""
config = Configuration(shared.CONFIG_FILE)
configWebPages = config.getWebPages()
port = config.getPort()
shared.periodInSeconds = config.getPeriod()

"""Check URL's"""
if len(configWebPages) > 0 and shared.periodInSeconds > 0:
   for key in configWebPages.keys():
      shared.webPages.append(WebPage(key, shared.periodInSeconds, configWebPages[key]))  
   

   Handler = ServerHandler
   
   httpd = SocketServer.ThreadingTCPServer(("", int(port)), Handler)
   
   print "serving at port", port
   try:
      httpd.serve_forever()   
   except KeyboardInterrupt:
      print "Stopping App"
      httpd.shutdown()
      for page in shared.webPages:
         page.stop()          
      sys.exit()   
else:
   logger.exception('Error with configurations, Application shutting down')

  
           

