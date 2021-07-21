const express = require('express')
const mysql = require('mysql')
const cors = require('cors')

const app = express()

app.use(cors())
app.use(express.json())

const db = mysql.createConnection({
    user: 'testuser',
    password: 'test123',
    host: 'localhost',
    database: 'netmonitordb',
    timezone: 'Z'
})

app.get('/sms', (req, res) =>{
    db.query('SELECT * FROM smslogs ORDER BY timestamp DESC LIMIT 60',(err,result) => {
        if(err){
            console.log(err)
        }else{
            res.send(result)
            console.log(result)
        }
    })
})

app.get('/voice', (req, res) =>{
    db.query('SELECT * FROM voicelogs ORDER BY timestamp DESC LIMIT 60',(err,result) => {
        if(err){
            console.log(err)
        }else{
            res.send(result)
            console.log(result)
        }
    })
})

app.get('/data', (req, res) =>{
    db.query('SELECT * FROM datalogs ORDER BY timestamp DESC LIMIT 60',(err,result) => {
        if(err){
            console.log(err)
        }else{
            res.send(result)
            console.log(result)
        }
    })
})

app.get('/outages', (req, res) =>{
    db.query('SELECT * FROM outages ORDER BY severity DESC',(err,result) => {
        if(err){
            console.log(err)
        }else{
            res.send(result)
            console.log(result)
        }
    })
})

app.listen(3005, () => {
    console.log("Network KPI Monitoring Server is running...")
})