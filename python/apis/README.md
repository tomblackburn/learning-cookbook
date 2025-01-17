# Let's get some of the basics out of the way

An API (application programming interface) is a setup to allow two pieces of software to communicate. 

![images/api-basic.png](images/api-basic.png)

In the above, crude example, the API is an interface for these pieces of software to communicate with one another. This communication between software is typically one direction. This means one software system will do all of the talking, and the other software system will request data. You could say server (backend) and client (frontend).

Let’s say we are building an app to store information about drinks, and we want to get information about a particular drink. I’ll likely have a server, let’s say written in Python, that manages this data by connecting to a database. The client can then request this data from the server, the server gets the information from the database, and then returns the data to the client.

Every software system is a little different, therefore there are challenges with software communication. It helps if we are communicating using some standard notion. This nothing is usually JSON.

## JSON
**JSON** is a standard notation used to communicate between software. XML is also a popular notation to use, but is a lot less favorable compared to JSON at the moment.

JSON is built on two structures:

- A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
- An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.

[https://www.json.org/json-en.html](https://www.json.org/json-en.html)

## Endpoints
Our server software doesn’t just open up everything for other software to use. Instead, the developers carefully choose specific things that should be exposed for other software to consume. These things are exposed as API endpoints. 

So for the backend we might create an API endpoint and it will look like this: /drinks/<id> where the id could be any ID to grab information about a particular drink. 

Now you might be asking, What’s with the slashes? That’s where the REST part of this comes in. **REST** (representational state transfer) is a particular type of API that allows the transfer of data (also known as **state**, as the acronym would imply) over the internet. So these slashes are actually a URL. 

The full endpoint might be used like so: itstomblackburn.com/drinks/5.

## Why the Complexity
Instead of having a front end talk to a back end which talks to the database, why don’t you just simplify and remove the middle man (the server) and just have the client do it?

- **Security** - The most popular front end language is JavaScript, which in front end web development has no concept of security. On a side note, we can include authentication and authorization with our API so only certain people using the front end applications can access sensitive data. 
- **Versatility** - with a single backend, we can build numerous front ends that have the single purpose of presenting and interacting with data. This means we could have a website, a mobile application, and a desktop application, and they’re all going to work properly with the same data because the data processing is all done on the back end. 
- **Modularity** - We can swap out the backend without having anyone notice or have to update an application. As long as the backend exposes the same API. This is a perfect example of abstraction. We are abstracting away the data processing and always working with a consistent interface (a REST API that uses JSON). 
- **Interoperability** - If desired, your API can be public for any developers to consume. This means that the frontend and backend do not have to be by the same developer. There are tons of public APIs out there that we can use to create cool apps. You could make an instagram browser, or a cryptocurrency trading bot, or a machine learning model based off of YouTube analytics. 

# REST API Methods
When you open Chrome or Firefox or your browser of choice, and you go to a website like stackoverflow.com,behind the scenes you’re making a **GET** request. And the website is listening for requests at the root (/) and returns HTML. 

You can see all of this in the developer tools of any modern browser. 
The request method is GET, and the content-type is text/html.

To get JSON, there is actually another web address that you can use, api.stackexchange.com, that has endpoints that return JSON. 

- **GET** is the first method to understand and is one of the most common.
- **POST** is another method, which is used when you submit forms on web pages. APIs also support POST and this is the method you usually use when you want to add or modify data, such as adding a new answer to a question on Stack Overflow. 
