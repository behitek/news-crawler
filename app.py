from flask import Flask, request, render_template

from news_crawler import crawl

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            url = request.form['url']
            res = crawl(url)
            if res.get('error') != '':
                return render_template('index.html',
                                       error=res.get('error'))
            else:
                return render_template('index.html',
                                       title=res.get('title'),
                                       content=res.get('content'),
                                       url=res.get('url'),
                                       keywords=res.get('keywords'),
                                       published_date=res.get('published_date'),
                                       top_img=res.get('top_img'))
        except:
            return render_template('index.html', error='Hệ thống quá tải, vui lòng thử lại sau.')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
