const Cors = require('cors');
var redis = require('redis');
let redis_host = "redis-11422.c62.us-east-1-4.ec2.cloud.redislabs.com"
let redis_port = 11422
const axios = require('axios');
let redis_password = "AFahzbIs3wTxs0VMPnvTqkuqyoZOWXwV"
var client = redis.createClient({ host: redis_host, port: redis_port, password: redis_password })
const express = require("express");
const app = express();
app.use(Cors())
let port = process.env.PORT || 3000;
setInterval(() => {
    let obj = { 'news': [] }
    client.get("all_news", async (err, resp) => {
        let data = JSON.parse(resp);
        for (let i in data['news']) {
            let articles = [];
            for (let article of data['news'][i]['articles']) {
                let innerObj = {
                    'description': article['description'],
                    'url': article['url'], 'title': article['title'],
                    'publishedAt': article['publishedAt'], 'urlToImage': article['urlToImage']
                }
                if (article["urlToImage"].includes("./img")) {
                    let response = await axios.post('https://hnews-image.herokuapp.com/image', { 'url': article['url'] });
                    if (response['data']['lead_image_url'] !== undefined) {
                        innerObj['urlToImage'] = response['data']['lead_image_url'];
                    }
                    else {
                        let arr = innerObj["urlToImage"].split("/");
                        innerObj["urlToImage"] = './assets/img/' + arr[2];
                    }
                    // console.log(innerObj);
                }
                articles.push(innerObj);
            }
            data['news'][i] = {'status': 'ok', 'articles': articles};
        }
        // console.log(data);
        obj.news = data['news'];
        client.set('enriched_news',JSON.stringify(obj));
    })
}, 900000)
app.get("/all", (req, res) => {
    client.get('enriched_news', (err, resp) => {
        let data = JSON.parse(resp);
        res.send(data['news'][0]['articles']);
    })
});

app.get("/general", (req, res) => {
    client.get('enriched_news', (err, resp) => {
        let data = JSON.parse(resp);
        res.send(data['news'][1]['articles']);
    })
});

app.get("/business", (req, res) => {
    client.get('enriched_news', (err, resp) => {
        let data = JSON.parse(resp);
        res.send(data['news'][2]['articles']);
    })
});

app.get("/entertainment", (req, res) => {
    client.get('enriched_news', (err, resp) => {
        let data = JSON.parse(resp);
        res.send(data['news'][3]['articles']);
    })
});

app.get("/health", (req, res) => {
    client.get('enriched_news', (err, resp) => {
        let data = JSON.parse(resp);
        res.send(data['news'][4]['articles']);
    })
});

app.get("/science", (req, res) => {
    client.get('enriched_news', (err, resp) => {
        let data = JSON.parse(resp);
        res.send(data['news'][5]['articles']);
    })
});

app.get("/technology", (req, res) => {
    client.get('enriched_news', (err, resp) => {
        let data = JSON.parse(resp);
        res.send(data['news'][6]['articles']);
    })
});

app.get("/sport", (req, res) => {
    client.get('enriched_news', (err, resp) => {
        let data = JSON.parse(resp);
        res.send(data['news'][7]['articles']);
    })
});

app.get("/offbeat", (req, res) => {
    client.get('enriched_news', (err, resp) => {
        let data = JSON.parse(resp);
        res.send(data['news'][8]['articles']);
    })
});

app.get("/keyNews", (req, res) => {
    client.get('keyNews', (err, resp) => {
        let data = JSON.parse(resp);
        res.send(data);
    })
});

app.get("/backImg", (req, res) => {
    client.get('all_news', (err, resp) => {
        let data = JSON.parse(resp);
        let x = { 'url': data['backImg'] };
        res.send(x);
    })
})

app.get("/joke", (req, res) => {
    const options = {
        headers: { 'Accept': 'application/json' }
    }
    axios.get('https://icanhazdadjoke.com/', options).then(response => {
        res.send(response.data)
    })
})

app.listen(port, () => {
    console.log(`Example app is listening on port http://localhost:${port}`)
});