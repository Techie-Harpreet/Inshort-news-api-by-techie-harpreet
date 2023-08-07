# Inshorts News API [Unofficial]

---

This API is capable of fetching news contents from various sources as gathered by Inshorts app.

## News Categories

This API supports category wise news. Here is a complete list of all categories.

1. all
2. national //Indian News only
3. business
4. sports
5. world
6. politics
7. technology
8. startup
9. entertainment
10. miscellaneous
11. hatke
12. science
13. automobile

---

## Usage

Make a get request specifying the category of news you want

```
https://inshorts.deta.dev/news?category={category_name}
```

Example - https://inshorts.deta.dev/news?category=science

---

## Response Format

The response JSON Object looks something like this -

```JSON
    {
    "category": "sports",
    "data": [
    {
    "author": "Anmol Sharma",
    "content": "West Indies defeated India by two wickets in the second T20I in Guyana to take a 2-0 lead in the five-match series. India have lost two international matches in a row against West Indies for the first time in more than 12 years. West Indies wicketkeeper Nicholas Pooran top-scored in the second T20I with 67(40).",
    "date": "06 Aug 2023,Sunday",
    "imageUrl": "https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2023/08_aug/6_sun/img_1691343971001_611.jpg?",
    "readMoreUrl": "https://www.espncricinfo.com/series/india-in-west-indies-2023-1381201/west-indies-vs-india-2nd-t20i-1381218/live-cricket-score?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
    "time": "11:40 pm",
    "title": "India lose 2 int'l matches in a row against West Indies for the first time in 12 years",
    "url": "https://www.espncricinfo.com/series/india-in-west-indies-2023-1381201/west-indies-vs-india-2nd-t20i-1381218/live-cricket-score?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts "
    },

    {
    "author": "Aditya Nair",
    "content": "Aprilia Racing's Aleix Espargaro won the British MotoGP on the final lap from world champion Francesco Bagnaia. Espargaro's late move on the championship leader was further aided by light rain on the circuit during the closing stages. \"It was tricky. I tried to push but I was on the limit...Finishing second is a great result,\" said Bagnaia after the race. ",
    "date": "06 Aug 2023,Sunday",
    "imageUrl": "https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2023/08_aug/6_sun/img_1691341860963_692.jpg?",
    "readMoreUrl": "https://www.news18.com/amp/sports/aleix-espargaro-claims-dramatic-british-motogp-win-in-last-lap-to-pip-world-champion-francesco-bagnaia-8518417.html?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
    "time": "11:01 pm",
    "title": "Espargaro wins British GP overtaking World Champion on last lap",
    "url": "https://www.news18.com/amp/sports/aleix-espargaro-claims-dramatic-british-motogp-win-in-last-lap-to-pip-world-champion-francesco-bagnaia-8518417.html?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts "
    }
    ],
    "success": true
    }
```

---

## Setup

Install all dependencies listed in _requirements.txt_ file.

1. To install all dependencies run -

   ```bash
   $ pip install -r requirements.txt
   ```

2. Start the server

   ```bash
   $ python app.py
   ```

---

## Apps using this API

#### [Telegram Channel](https://telegram.dog/inshortschannel) of Inshorts News

## [![Telegram Channel](https://img.shields.io/endpoint?color=neon&style=flat-square&url=https%3A%2F%2Ftg.sumanjay.workers.dev%2Finshortschannel)](https://telegram.dog/inshortschannel)

### You can fork the repo and deploy on VPS, Heroku or Vercel :)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cyberboysumanjay/Inshorts-News-API/tree/master)

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/cyberboysumanjay/Inshorts-News-API/tree/master)

---

#### :star: the Repo in case you liked it :)

#### Made with :heart: in India

# © [Techie Harpreet](https://harpreetsinghbansal.com/)
