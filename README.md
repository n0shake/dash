![Build Status](https://travis-ci.com/abhishekbanthia/Dash.svg?token=Acx5xfwTcZkSxUpPzh9h&branch=master)

# DoorDash-API

**Disclaimer**: I'm a huge DoorDash fan and this is purely an activity out of curiosity and laziness.

# Major 🔑

Ever since moving to the Bay Area, DoorDash has found a loyal customer in me. It's always fun reverse-engineering REST APIs, and also understanding how DoorDash interacts with the Internet. Door Dash encrypts its network traffic using SSL, but this is really easy to get around using a simple Man-in-the-middle attack.

# Design

Have been meaning to learn Python since quite some time, this gives me an opportunity to do that. Since this is a Python library, this is meant to be used in CLI environments. The API is really really rough around the edges, though I have tried to handle failing conditions gracefully.

# Pre-requisites

You'll need an DoorDash account.

# Using

1. Authenticate to DoorDash using your credentials
2. From the list of suggestions, select one (you can sort based on the rating, price, and the availability)
3. A list of restaurants based on your suggestion will be displayed
4. On selecting a restaurant, a menu will be displayed. Select the items you'll like to add to your cart, quantity, special instructions etc and you're set.

# Future

How about ordering DoorDash from your menubar?
