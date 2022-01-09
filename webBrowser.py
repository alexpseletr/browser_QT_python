import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl , Qt

app = QApplication(sys.argv)

webBrowser = QWebEngineView()

#Some line here to delete the contextMenu
# webView.settings().setAttribute(QWebEngineSettings.)
# webView.javaScriptConsoleMessage
# webView.load(QUrl('https://www.baidu.com'))
# webBrowser.load(QUrl('http://google.com'))

webBrowser.setContextMenuPolicy(Qt.NoContextMenu)

webBrowser.load(QUrl("http://google.com"))

# if  webBrowser.loadFinished.success:
#     print("webBrowser.loadFinished()")

# html = """
#         <!DOCTYPE HTML>
#             <html>
#                 <head>
#                 </head>
#                 <body>
#                     <h1>Loading address...</h1>
#                 </body>
#             </html>
#         """

# webBrowser.setHtml(html)

webBrowser.setWindowTitle("my title")

webBrowser.show()

sys.exit(app.exec_())
