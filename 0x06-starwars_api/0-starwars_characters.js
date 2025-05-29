#!/usr/bin/node

let args = process.argv.slice(2);
if (args[0] == undefined) {
    // if no argument
    console.log('Usage: ./0-starwars_characters movie_id')
    process.exit();
} else if (args.length !== 1) {
    process.exit(); 
}

let url = 'https://swapi-api.alx-tools.com/api/films/' + args[0];
let request = require('request');
request(url, function (error, response, body) {
    if (error) {
        console.log('Request film error')
    }
    if (response.statusCode === 200) {
        let obj = JSON.parse(body);
        let characters = obj['characters'];
        characters.forEach(function (character) {
            request(character, function(error2, response2, body2) {
                if (error2) {
                    console.log('Request character error')
                }
                if (response2.statusCode === 200) {
                    let character2 = JSON.parse(body2);
                    console.log(character2['name']);
                }
            });
        });
    }
});
