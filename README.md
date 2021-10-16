# Overview

This is a web app called Learning Log that allows administrators to log the topics they're interested in and to make journal entries as they learn about each topic. Once logged in, an admin should be able to create new topics, add new entries, and read and edit existing entries. 

I wrote this software because when you learn about a topic, keeping a journal of what you've learned can be helpful in tracking and revisiting information. A good app makes this process efficient.

[Demo Video](https://youtu.be/jXhmyM7YZjE)

# Web Pages

- base.html is a parent template from which all pages inherit common tags and attributes using the template tag mini-language included with Django
- index.html is the home page for the web app where users will land when they visit the base url
- topics.html shows all topics recorded in the learning log by the admin
- topic.html shows all entries for a selected topic, which populates the page in reverse order from the newest entry first to the oldest entry last

# Development Environment

- Visual Studio Code
- Python 3.8.10 32-bit
- Django 3.2.8
- Git / GitHub

# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/en/3.2/)
* [Django Crash Course Tutorial by Dennis Ivy](https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
* [Python Crash Course Book - Chapter 18](https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593276036)

# Future Work

* Add styling
* Add a login page
* Add some user functionality