# Project 1 - Movie Trailer Website

Movie Trailer Website is a website generated through python code that shows the current top 20 most popular movies information and trailers.
The website was designed as part of the Udacity Web Full Stack Nanodegree.

# Getting Started

To be able to generate the website, Python 2.7.15 is required. For more information about how to install Python, please visit https://www.python.org/about/gettingstarted/

# Usage

It is possible to generate the website using a predefined collection of movies stored at `movie_list.json` file. To do so, navegate to the root directory and execute
```
python entertainment_center.py
```
You can also update `movie_list.json` before generating the site by querying The Movie Database API. To do so, retrieve an API key from The Movie Database website and modify `utils.py` with it. For more information about how to retrieve it, visit https://www.python.org/about/gettingstarted/. After updating `utils.py` with your key, run

```
python utils.py
```

to update `movie_list.json`

# Authors
* Udacity Team
* Felipe Freitas Fonseca

# License

This project is licensed under the MIT License. For more information about it, please visit https://opensource.org/licenses/MIT
