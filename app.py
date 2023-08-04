import feedparser
from flask import Flask, render_template, session, request, redirect, url_for
import logging
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rss_feeds.db'
db = SQLAlchemy(app)

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True, nullable=False)

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def defer_image_loading(content):
    # Replace src with data-src for images
    return re.sub(r'<img (.*?)src="(.*?)"', r'<img \1data-src="\2"', content)



with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return unified_feed()


@app.route('/add_feed', methods=['POST'])
def add_feed():
    feed_url = request.form.get('rssURL')
    if not Feed.query.filter_by(url=feed_url).first():  # check if URL is not already in the database
        feed = Feed(url=feed_url)
        db.session.add(feed)
        db.session.commit()
    return redirect(url_for('grouped_feed'))


@app.route('/remove_feed/<path:feed_url>', methods=['GET'])
def remove_feed(feed_url):
    feed = Feed.query.filter_by(url=feed_url).first()
    if feed:
        db.session.delete(feed)
        db.session.commit()
    return redirect(url_for('grouped_feed'))




@app.route('/unified')
def unified_feed():
    # Fetch all feed URLs from the database
    feed_urls = [feed.url for feed in Feed.query.all()]

    all_entries = []
    for feed_url in feed_urls:
        parsed_feed = feedparser.parse(feed_url)
        for entry in parsed_feed.entries:
            if hasattr(entry, 'content'):
                entry.content[0].value = defer_image_loading(entry.content[0].value)
            elif hasattr(entry, 'summary'):
                entry.summary = defer_image_loading(entry.summary)
        all_entries.extend(parsed_feed.entries)

    # Sort entries by published date, if available
    sorted_entries = sorted(all_entries, key=lambda e: e.get('published_parsed', ''), reverse=True)

    return render_template('unified.html', entries=sorted_entries)

@app.route('/grouped')
def grouped_feed():
    # Fetch all feed URLs from the database
    feed_urls = [feed.url for feed in Feed.query.all()]

    feed_data = {}
    for feed_url in feed_urls:
        parsed_feed = feedparser.parse(feed_url)
        feed_data[feed_url] = parsed_feed.entries

    return render_template('grouped.html', feed_data=feed_data)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
