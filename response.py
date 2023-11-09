from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    url = f'https://www.example.com/{path}'

    headers = {key: value for (key, value) in request.headers if key != 'Host'}
    response = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
        stream=True,
    )

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in response.raw.headers.items() if name.lower() not in excluded_headers]
    content = response.raw.read(decode_content=True)

    return Response(content, response.status_code, headers)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

