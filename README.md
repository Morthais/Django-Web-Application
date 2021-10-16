# Overview

{Provide a description the web app that you wrote. Describe how to start a test server on your computer and what website to open up to see the first page of the app.}

This is a web app called Learning Log that allows administrators to log the topics they're interested in and to make journal entries as they learn about each topic. Once logged in, an admin should be able to create new topics, add new entries, and read and edit existing entries. 

I wrote this software because when you learn about a topic, keeping a journal of what you've learned can be helpful in tracking and revisiting information. A good app makes this process efficient.

{Provide a link to the YouTube demonstration.  It will be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

{Describe each of the web pages you created and how the web app transitions between each of them.  Also describe what is dynamically created on each page.}
- base.html is a parent template from which all pages inherit common tags and attributes using the template tag mini-language included with Django
- index.html is the home page for the web app where users will land when they visit the base url
- topics.html shows all topics recorded in the learning log
- topic.html shows an entry for a selected topic

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

{Make a list of things that you need to fix, improve, and add in the future.}
* Add styling
* Add a login page
* Add some user functionality