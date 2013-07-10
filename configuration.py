#Author: Mikhael Santos
from ConfigParser import SafeConfigParser
import configuration, shared, logging
logger = logging.getLogger("monitor")
"""Class that represents the configuration file"""
class Configuration(object):
	def __init__(self, file):
		self.__configParser = SafeConfigParser()
		self.__configParser.read(file)
	
	"""Gets time period to define checking interval"""
	def getPeriod(self):
		""""Verify if period is already in memory"""
		try: 
			if not hasattr(self, 'period'):	
				self.__period = self.__configParser.get(shared.CHECKING_PERIOD_HEADER,shared.PERIOD_VALUE)
			return self.__period
		except Exception,e:
			return -1
	def getPort(self):
		""""Verify if period is already in memory"""
		try: 
			if not hasattr(self, 'port'):	
				self.__port= self.__configParser.get(shared.ACCESS_PORT_HEADER,shared.PORT)
			return self.__port
		except Exception,e:
			return -1	
		
	"""Gets the Web Pages Configured in Config File	
	returning a dicionary with websites and options"""
	def getWebPages(self):
		webSites = {}
		try:
			for section_name in self.__configParser.sections():
				if section_name != shared.CHECKING_PERIOD_HEADER and section_name != shared.ACCESS_PORT_HEADER:        
					print 'Section:', section_name
					print '  Options:', self.__configParser.options(section_name)
					webSiteOptions = {}
					for name, value in self.__configParser.items(section_name):
						print '  %s = %s' % (name, value)
						webSiteOptions[name] = value
					webSites[section_name] = webSiteOptions
		except Exception, e:
			logger.error("Obtaining Sections and Obtions")
		print webSites
		return webSites
