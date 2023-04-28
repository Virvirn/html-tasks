from flask import Flask

app = Flask(__name__)


@app.route('/carousel')
def result():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Марс</title>
                        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" 
                        integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" 
                        crossorigin="anonymous"></script>
                        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.min.js" 
                        integrity="sha384-Atwg2Pkwv9vp0ygtn1JAojH0nYbwNJLPhwyoVbhoPwBhjQPR5VtM2+xf0Uwh9KtT" 
                        crossorigin="anonymous"></script>
                      </head>
                      <body>
                        <div id="carousel" class="carousel slide">
                          <div class="carousel-inner">
                            <div class="carousel-item active">
                              <img src="static/img/mars.jpg" class="d-block w-100">
                            </div>
                            <div class="carousel-item">
                              <img src="static/img/mars2.png" class="d-block w-100">
                            </div>
                            <div class="carousel-item">
                              <img src="static/img/mars-1.jpg" class="d-block w-100">
                            </div>
                          </div>
                          <button class="carousel-control-prev" type="button" data-bs-target="#carousel" 
                          data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Предыдущий</span>
                          </button>
                          <button class="carousel-control-next" type="button" data-bs-target="#carousel" 
                          data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Следующий</span>
                          </button>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')