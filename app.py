from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html',title='LK')


@app.route('/price')
def price():
    return render_template('price.html',title='Price')

@app.route('/studio')
def studio():
    return render_template('studio.html',title='Studio')

@app.route('/portfolio')
def portfolio():
    street_folders = os.listdir('./static/portfolio/Street')
    street_paths = ['/portfolio/Street/'+street_folder for street_folder in street_folders]
    street_photos = [street_path+'/'+os.listdir('./static/'+street_path)[0] for street_path in street_paths]

    studio_folders = os.listdir('./static/portfolio/Studio')
    studio_paths = ['/portfolio/Studio/'+studio_folder for studio_folder in studio_folders]
    studio_photos = [studio_path+'/'+os.listdir('./static/'+studio_path)[0] for studio_path in studio_paths]
    print(studio_photos)
    return render_template('portfolio.html',title='Portfolio',street_photos=street_photos,studio_photos=studio_photos)

@app.route('/portfolio/<collection>')
def sub_portfolio(collection):
    titles = os.listdir('./static/portfolio/'+collection)
    covers = []
    collections =[]
    for title in titles:
        covers.append('portfolio/'+collection+'/'+title+'/'+os.listdir('./static/portfolio/'+collection+'/'+title)[0])
        collections.append(collection)
    return render_template('sub_portfolio.html',title='Portfolio',titles=titles,covers=covers,zip=zip,collections=collections)


@app.route('/portfolio/<collection>/<shooting>')
def show_collection(collection,shooting):
    coll_fld = f'./static/portfolio/{collection}/'
    photos_name = os.listdir(coll_fld+shooting)
    photos_path = ['portfolio/'+collection+'/'+shooting+f'/{photo}' for photo in photos_name]


    return render_template('show_collection.html',title=collection,data=photos_path)


if __name__ == '__main__':
    app.run(debug=True)