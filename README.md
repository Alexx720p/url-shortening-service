# url-shortening-service

https://roadmap.sh/projects/url-shortening-service

This API was made using Django Rest Framework and Sqlite3 and I used Apidog to test it

# How to use it
- Clone the repo in your local env and install the requirements
- Run the server using the following command: >python manage.py runserver

# These are the five endpoints you can make requests to:
- Create a new short URL: POST /shorten/ JSON: {<p> "original_url": "https://example.com/long/url"</p>}
- Retrieve a shortened URL: GET /shorten/url_short_code/
- Update a shortened URL: PUT /shorten/url_short_code/update/ {<p> "original_url": "https://example.com/new/url"</p>}
- Delete a shortened URL: DELETE /shorten/url_short_code/delete/
- Get the stats and info of a shortened URL: GET /shorten/url_short_code/stats/

