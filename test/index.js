const Cors = require('cors');
var redis = require('redis');
let redis_host = "redis-11422.c62.us-east-1-4.ec2.cloud.redislabs.com"
let redis_port = 11422
let redis_password = "AFahzbIs3wTxs0VMPnvTqkuqyoZOWXwV"
var client = redis.createClient({ host: redis_host, port: redis_port, password: redis_password })
const express = require("express");
const app = express();
app.use(Cors())
let port = process.env.PORT || 3000;
app.get("/all", (req, res) => {
    client.get('all_news',(err, resp)=>{
        let data = JSON.parse(resp);
        res.send(data['news'][0]['articles']);
    })
});

app.get("/general", (req, res) => {
    client.get('all_news',(err, resp)=>{
        let data = JSON.parse(resp);
        res.send(data['news'][1]['articles']);
    })
});

app.get("/business", (req, res) => {
    client.get('all_news',(err, resp)=>{
        let data = JSON.parse(resp);
        res.send(data['news'][2]['articles']);
    })
});

app.get("/entertainment", (req, res) => {
    client.get('all_news',(err, resp)=>{
        let data = JSON.parse(resp);
        res.send(data['news'][3]['articles']);
    })
});

app.get("/health", (req, res) => {
    client.get('all_news',(err, resp)=>{
        let data = JSON.parse(resp);
        res.send(data['news'][4]['articles']);
    })
});

app.get("/science", (req, res) => {
    client.get('all_news',(err, resp)=>{
        let data = JSON.parse(resp);
        res.send(data['news'][5]['articles']);
    })
});

app.get("/technology", (req, res) => {
    client.get('all_news',(err, resp)=>{
        let data = JSON.parse(resp);
        res.send(data['news'][6]['articles']);
    })
});

app.get("/sport", (req, res) => {
    client.get('all_news',(err, resp)=>{
        let data = JSON.parse(resp);
        res.send(data['news'][7]['articles']);
    })
});

app.get("/offbeat", (req, res) => {
    client.get('all_news',(err, resp)=>{
        let data = JSON.parse(resp);
        res.send(data['news'][8]['articles']);
    })
});

app.get("/keyNews", (req, res) => {
    client.get('keyNews',(err, resp)=>{
        let data = JSON.parse(resp);
        res.send(data);
    })
});

app.listen(port, () => {
    console.log(`Example app is listening on port http://localhost:${port}`)
});