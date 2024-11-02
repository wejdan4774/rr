from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # محتوى الصفحة
        html = """
        <!DOCTYPE html>
        <html lang="ar">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>تعلم الإنجليزية</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                    background-color: #f4f4f4;
                }
                h1 {
                    color: #4CAF50;
                }
                table {
                    margin: auto;
                    border-collapse: collapse;
                    width: 50%;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                }
                th {
                    background-color: #4CAF50;
                    color: white;
                }
            </style>
        </head>
        <body>
            <h1>مرحبًا بكم في موقع تعلم الإنجليزية!</h1>
            <p>إليك بعض الكلمات الإنجليزية ومعانيها:</p>
            <table>
                <tr>
                    <th>الكلمة الإنجليزية</th>
                    <th>المعنى بالعربية</th>
                </tr>
                <tr>
                    <td>Hello</td>
                    <td>مرحبا</td>
                </tr>
                <tr>
                    <td>Goodbye</td>
                    <td>وداعا</td>
                </tr>
                <tr>
                    <td>Thank you</td>
                    <td>شكرا لك</td>
                </tr>
                <tr>
                    <td>Please</td>
                    <td>من فضلك</td>
                </tr>
            </table>
        </body>
        </html>
        """
        self.wfile.write(bytes(html, "utf8"))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)  # استخدم المنفذ 8000
    httpd = server_class(server_address, handler_class)
    print("يعمل على http://localhost:8000/")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
