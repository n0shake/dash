![Build Status](https://travis-ci.com/abhishekbanthia/Dash.svg?token=Acx5xfwTcZkSxUpPzh9h&branch=master)

# Dash - Python Client to browse DoorDash from your command line

**Disclaimer**: I'm a huge DoorDash fan and this is purely an activity out of curiosity.

![Screenshot](https://github.com/abhishekbanthia/dash/blob/master/Screenshot.png)

[Link to Demo](https://asciinema.org/a/a6wfl2cfepory53795a2iq14b)

# Usage

Build the Dash.py using your credentials and follow steps to add items to your cart.

`$ python Dash.py frodo.baggins16@yandex.com frodobaggins`


# Why

Ever since moving to the Bay Area, DoorDash has found a loyal customer in me. It's always fun reverse-engineering REST APIs; I also wanted to understand how DoorDash interacts with the Internet. Door Dash encrypts its network traffic using SSL, but this is really easy to get around using a simple Man-in-the-middle attack.

# Design

Have been meaning to learn Python since quite some time, this gives me an opportunity to do that. Since this is a Python library, this is meant to be used in CLI environments. The API is really really rough around the edges, though I have tried to handle failing conditions gracefully.

# Pre-requisites

You'll need an DoorDash account and DoorDash should be available at your location.

# Using

1. Authenticate to DoorDash using your credentials
2. From the list of suggestions, select one (you can sort based on the rating, price, and the availability)
3. A list of restaurants based on your suggestion will be displayed
4. On selecting a restaurant, a menu will be displayed. Select the items you'll like to add to your cart, quantity, special instructions etc and you're set.

