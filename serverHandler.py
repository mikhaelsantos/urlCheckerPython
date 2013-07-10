import SimpleHTTPServer, shared

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def do_GET(self):
        if self.path == '/css/bootstrap.css':
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        else:    
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("<html><head><meta http-equiv='refresh' content='%s'><link rel='stylesheet' href='css/bootstrap.css' type='text/css' /><title> URL Checker</title></head>"%shared.periodInSeconds)
            self.wfile.write("<body><H1>URL Checker</H1>")
            self.wfile.write("<p>Automatic refresh every %s seconds</p>"%shared.periodInSeconds)
            self.wfile.write("<table class='table table-bordered'>")  
            self.wfile.write("<thead>")
            self.wfile.write("<tr>")
            self.wfile.write("<th>URL</th>")
            self.wfile.write("<th>Status Code</th>")
            self.wfile.write("<th>Content Validation</th>")
            self.wfile.write("<th>Time</th>")
            self.wfile.write("</tr>")
            self.wfile.write("</thead>")    
            for page in shared.webPages:
                result = page.getLastResult()
                self.wfile.write("<tbody>")                
                if len(result) != 0:               
                    if result['status'] != 200:
                        self.wfile.write("<tr class='error'>") 
                    elif not result['content']:
                        self.wfile.write("<tr class='warning'>") 
                    else:
                        self.wfile.write("<tr class='success'>") 
                    for key in result:
                        self.wfile.write("<td> %s</td>" % result[key])
                    self.wfile.write("</tr>") 
                self.wfile.write("</tbody>")
            self.wfile.write("</table>")     
            self.wfile.write("</body></html>")
            self.wfile.close()


