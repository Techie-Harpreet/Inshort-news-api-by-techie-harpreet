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
http://127.0.0.1:5000/news?category={category_name}
```

Example - https://inshorts.deta.dev/news?category=science

---

## Response Format in English

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




---

## Response Format in Hindi

The response JSON Object looks something like this -

```JSON
    {
    "category": "all",
    "data": [
    {
    "author": "चंद्रमणि झा",
    "content": "वेस्टइंडीज़ ने रविवार को गुयाना में दूसरे टी20I मैच में भारत को 2 विकेट से हराकर 5 मैचों की सीरीज़ में 2-0 की बढ़त बना ली। इसके साथ ही भारत को 12 साल में पहली बार वेस्टइंडीज़ के खिलाफ लगातार 2 अंतर्राष्ट्रीय मैचों में हार मिली है। दूसरे टी20I में वेस्टइंडीज़ के विकेटकीपर-बल्लेबाज़ निकोलस पूरन ने सर्वाधिक 67(40) रन बनाए।",
    "date": "06 Aug 2023,Sunday",
    "imageUrl": "https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2023/08_aug/6_sun/img_1691344112939_10.jpg?",
    "readMoreUrl": "https://www.espncricinfo.com/series/india-in-west-indies-2023-1381201/west-indies-vs-india-2nd-t20i-1381218/live-cricket-score?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
    "time": "11:43 pm",
    "title": "भारत को 12 साल में पहली बार वेस्टइंडीज़ के खिलाफ लगातार 2 अंतर्राष्ट्रीय मैचों में मिली हार",
    "url": "https://www.espncricinfo.com/series/india-in-west-indies-2023-1381201/west-indies-vs-india-2nd-t20i-1381218/live-cricket-score?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts "
    },

    {
    "author": "अनिल कुमार",
    "content": "नूंह हिंसा को लेकर रविवार को गुरुग्राम (हरियाणा) में महापंचायत बुलाई गई जहां ज़िला बार असोसिएशन के पूर्व प्रधान कुलभूषण भारद्वाज ने मुख्यमंत्री मनोहर लाल खट्टर के इस्तीफे की मांग की। उन्होंने कहा, \"हमें योगी आदित्यनाथ जैसा मुख्यमंत्री चाहिए, नहीं तो मेवात को उत्तर प्रदेश में शामिल कर दें।\" गौरतलब है, इस हिंसा में 6 लोगों की मौत हुई थी।",
    "date": "07 Aug 2023,Monday",
    "imageUrl": "https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2023/08_aug/7_mon/img_1691378733539_698.jpg?",
    "readMoreUrl": "https://www.livehindustan.com/ncr/story-we-want-cm-like-yogi-adityanath-otherwise-merg-nuh-in-up-demand-raised-in-hindu-samaj-mahapanchayat-at-tighar-village-in-gurugram-8540118.amp.html?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
    "time": "10:52 am",
    "title": "हमें योगी जैसा सीएम चाहिए: नूंह हिंसा को लेकर गुरुग्राम बार असोसिएशन के पूर्व प्रधान कुलभूषण",
    "url": "https://www.livehindustan.com/ncr/story-we-want-cm-like-yogi-adityanath-otherwise-merg-nuh-in-up-demand-raised-in-hindu-samaj-mahapanchayat-at-tighar-village-in-gurugram-8540118.amp.html?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts "
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

#### :star: the Repo in case you liked it :)

#### Made with :heart: in India

# © [Techie Harpreet](https://harpreetsinghbansal.com/)
