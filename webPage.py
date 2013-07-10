#Author: Mikhael Santos
from threading import Timer
import httplib2, time, logging, shared

logger = logging.getLogger(shared.LOGGER)
"""Class that Represents a WebPage"""
class WebPage(object):
	def __init__(self, name, interval ,options):
		self.__options = options
		self.__interval = float(interval)
		self.__name = name
		self._timer = None
		self.is_running = False
		self.start()
		self.__results = {}
	def getLastResult(self):
		return self.__results
	"""Methode responsable for requesting URL and building result String"""
	def __verifyWebPage(self):		
		http = httplib2.Http()  
		results = {}
		results = {'name': self.__name}
		results = {'url': self.__options [shared.URL]}
		try:
			timerStart = time.time()
			response, content = http.request(self.__options[shared.URL])
			timerEnd = time.time()
			results['status'] = response.status
			if(response.status == 200):
				if(self.__validateContent(content)):
					results['content'] = True
				else:
					results['content'] = False
			else:
				results['content'] = False
			results['time'] = timerEnd - timerStart
			logger.info('%s', results) 
			
		except Exception, e:
			results['content'] = False
			results['time'] = -1
			results['status'] = 400
			logger.error(results)
		
		self.__results = results
		return self.__results
	
	"""Method responsabile for validating content with the content in config file"""
	def __validateContent(self, content):

		if content.find(self.__options[shared.CONTENT]) != -1 :
			self.__results['content'] = True
			return True
		self.__results['content'] = False
		return False
	
	"""Methode first call to flag that task is running"""
	def __run(self):
		self.is_running = False
		self.start()
		self.__verifyWebPage()
		
	"""Method that sets timer for call intervals and method to call repeatadly"""
	def start(self):
		if not self.is_running:
			self._timer = Timer(self.__interval, self.__run)
			self._timer.start()
			self.is_running = True
			
	"""Method responsabile for stopping the timer which to stops calling run"""
	def stop(self):
		self._timer.cancel()
		self.is_running = False	
	
		

		
