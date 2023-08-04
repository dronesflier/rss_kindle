## RSS Reader for Kindle

A simple and lightweight RSS reader designed for optimal "performance" on Kindle devices. Hosted and developed using Flask, this web-based application offers both unified and grouped views of RSS feeds.

### Features:
- **Unified Feed View**: Displays all RSS entries from various feeds sorted by date.
- **Grouped Feed View**: Categorizes entries based on their respective RSS sources.
- **Easy Feed Management**: Add or remove RSS feeds seamlessly.
- **Optimized for Kindle**: Designed with Kindle's unique display and performance characteristics in mind.
- **Persistent Storage**: Uses a SQLite database to save and manage the RSS feed URLs.

### Installation:

1. Clone the repository:
   ```
   git clone https://github.com/dronesflier/rss_kindle
   ```
2. Navigate to the project directory:
   ```
   cd rss_kindle
   ```
3. Install the required packages:
   ```
   pip3 install -r requirements.txt
   ```
4. Run the application:
   ```
   python3 app.py
   ```

### Usage:

- **Add Feed**: Enter the RSS feed URL and click the "Add Feed" button.
- **View Entries**: Choose between "Unified Feed" and "Grouped Feeds" from the navigation bar.
- **Remove Feed**: In the "Grouped Feeds" view, click the "Remove" button next to the feed name.

### Bugs:
- ***Incorrect size**: I tested this application on a kindle PaperWhite 7th Gen, and the web browser is a bit buggy; you need to sometimes when loading the page zoom in once by pinching and then out again to get the proper zoom

### Contributing:

Feel free to fork the repository and submit pull requests. All contributions are welcome!
