#!/usr/bin/node

const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/', (error, response, body) => {
    console.log(response.result)
});
