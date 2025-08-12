import express from "express";

const app = express();

app.get("/health",(req, res) => {
    res.send("<h1>Server Health Is Okay</h1>");
});

app.get("/home",(req, res) => {
    res.json({
        message :"Hello World!"
    })
});

app.get("/", (req,res) => {
    res.json({
        message :"This is Home Page"
    })
});


app.listen(4000,() => {
    console.log("Server is Listining on Port 4000");
});