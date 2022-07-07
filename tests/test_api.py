from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_movie():
    response = client.post(
        "/movie",
        json={"movie": "Toy Story"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            "Toy Story (1995)",
            "Antz (1998)",
            "Toy Story 2 (1999)",
            "Adventures of Rocky and Bullwinkle, The (2000)",
            "Emperor's New Groove, The (2000)",
            "Monsters, Inc. (2001)",
            "DuckTales: The Movie - Treasure of the Lost Lamp (1990)",
            "Wild, The (2006)",
            "Shrek the Third (2007)",
            "Tale of Despereaux, The (2008)",
            "Asterix and the Vikings (Astérix et les Vikings) (2006)",
            "Turbo (2013)",
            "Aladdin (1992)",
            "Boxtrolls, The (2014)",
            "Toy Story Toons: Hawaiian Vacation (2011)"
        ]
    }


def test_anime():
    response = client.post(
        "/anime",
        json={"movie": "Toy Story"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            "Death Note",
            "Death Note Rewrite",
            "Mousou Dairinin",
            "Higurashi no Naku Koro ni Kai",
            "Higurashi no Naku Koro ni Rei",
            "Mirai Nikki (TV)",
            "Mirai Nikki (TV): Ura Mirai Nikki",
            "Higurashi no Naku Koro ni",
            "Monster",
            "AD Police",
            "Higurashi no Naku Koro ni Kaku: Outbreak",
            "Zankyou no Terror",
            "Imawa no Kuni no Alice (OVA)",
            "Shigofumi",
            "Kara no Kyoukai 4: Garan no Dou"
        ]
    }


def test_book():
    response = client.post(
        "/anime",
        json={"book": "1984"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            [
                "Animal Farm",
                "George Orwell",
                "http://images.amazon.com/images/P/0451526341.01.MZZZZZZZ.jpg"
            ],
            [
                "The Handmaid's Tale",
                "Margaret Atwood",
                "http://images.amazon.com/images/P/0449212602.01.MZZZZZZZ.jpg"
            ],
            [
                "Brave New World",
                "Aldous Huxley",
                "http://images.amazon.com/images/P/0060809833.01.MZZZZZZZ.jpg"
            ],
            [
                "The Vampire Lestat (Vampire Chronicles, Book II)",
                "ANNE RICE",
                "http://images.amazon.com/images/P/0345313860.01.MZZZZZZZ.jpg"
            ],
            [
                "The Hours : A Novel",
                "Michael Cunningham",
                "http://images.amazon.com/images/P/0312243022.01.MZZZZZZZ.jpg"
            ],
            [
                "Fahrenheit 451",
                "Ray Bradbury",
                "http://images.amazon.com/images/P/3257208626.01.MZZZZZZZ.jpg"
            ],
            [
                "The Catcher in the Rye",
                "J.D. Salinger",
                "http://images.amazon.com/images/P/0316769487.01.MZZZZZZZ.jpg"
            ],
            [
                "Naked",
                "David Sedaris",
                "http://images.amazon.com/images/P/0316777730.01.MZZZZZZZ.jpg"
            ],
            [
                "The Hundred Secret Senses",
                "Amy Tan",
                "http://images.amazon.com/images/P/0399141146.01.MZZZZZZZ.jpg"
            ],
            [
                "The Drawing of the Three (The Dark Tower, Book 2)",
                "Stephen King",
                "http://images.amazon.com/images/P/0451163524.01.MZZZZZZZ.jpg"
            ]
        ]
    }


def test_game():
    response = client.post(
        "/game",
        json={"game": "Call of Duty"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            [
                "Call of Duty Classic",
                "['playstation-3', 'xbox-360']",
                "['Action', 'Shooter', 'First-Person', 'Third-Person', 'Historic', 'Tactical', 'Arcade']",
                "multiplayer"
            ],
            [
                "LawBreakers",
                "['playstation-4']",
                "['Third-Person', 'Arcade', 'Action', 'Shooter', 'First-Person', 'Tactical']",
                "multiplayer"
            ],
            [
                "Day of Defeat: Source",
                "['pc']",
                "['Action', 'Shooter', 'First-Person', 'Historic', 'Tactical', 'Arcade']",
                "multiplayer"
            ],
            [
                "Call of Duty: Black Ops",
                "['playstation-3', 'wii', 'ds']",
                "['Action', 'Shooter', 'First-Person', 'Historic', 'Tactical', 'Arcade']",
                "multiplayer"
            ],
            [
                "Call of Duty: Black Ops - Escalation",
                "['xbox-360']",
                "['Action', 'Shooter', 'First-Person', 'Historic', 'Tactical', 'Arcade']",
                null
            ],
            [
                "Call of Duty: Black Ops - Rezurrection",
                "['xbox-360']",
                "['Action', 'Shooter', 'First-Person', 'Historic', 'Tactical', 'Arcade']",
                null
            ],
            [
                "ShellShock 2: Blood Trails",
                "['pc', 'playstation-3']",
                "['Action', 'Shooter', 'First-Person', 'Third-Person', 'Historic', 'Arcade']",
                null
            ],
            [
                "Sniper Elite",
                "['xbox', 'playstation-2', 'pc']",
                "['Action', 'Shooter', 'Third-Person', 'Tactical', 'Historic']",
                "multiplayer"
            ],
            [
                "Sniper Elite III",
                "['pc', 'playstation-4', 'xbox-one']",
                "['Shooter', 'Historic', 'Action', 'Third-Person', 'Tactical']",
                null
            ],
            [
                "Tom Clancy's The Division 2",
                "['pc']",
                "['First-Person', 'Action', 'Shooter', 'Third-Person', 'Tactical']",
                "multiplayer"
            ]
        ]
    }


def test_manga():
    response = client.post(
        "/manga",
        json={"manga": "One Piece"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            [
                "Otona No Mondai",
                "https://avt.mkklcdnv6temp.com/35/l/4-1583471145.jpg"
            ],
            [
                "Girl X Girl X Boy",
                "https://avt.mkklcdnv6temp.com/18/v/5-1583472580.jpg"
            ],
            [
                "Become A Girl At Night",
                "https://avt.mkklcdnv6temp.com/42/i/18-1583498741.jpg"
            ],
            [
                "The Love Doctor",
                "https://avt.mkklcdnv6temp.com/22/s/14-1583490557.jpg"
            ],
            [
                "Milkman",
                "https://avt.mkklcdnv6temp.com/5/a/9-1583480288.jpg"
            ],
            [
                "Ijippari Yuugitai!",
                "https://avt.mkklcdnv6temp.com/12/m/16-1583493923.jpg"
            ],
            [
                "69",
                "https://avt.mkklcdnv6temp.com/9/p/7-1583476656.jpg"
            ],
            [
                "Bingo!",
                "https://avt.mkklcdnv6temp.com/18/c/7-1583476951.jpg"
            ],
            [
                "Hirano To Kagiura",
                "https://avt.mkklcdnv6temp.com/48/c/18-1583498973.jpg"
            ],
            [
                "Zenryaku, Yuri No Sono Yori",
                "https://avt.mkklcdnv6temp.com/22/u/9-1583480992.jpg"
            ]
        ]
    }


def test_music_bad():
    response = client.post(
        "/songs",
        json={"music": [{"name": "Come As You Are", "year": 1991}]},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "music"
                ],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


def test_music_good():
    response = client.post(
        "/songs",
        json={"songs": [{"name": "Come As You Are", "year": 1991}, {
            "name": "The Sign", "year": 1994}]}
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            {
                "name": "In the End",
                "year": 2000,
                "artists": "['Linkin Park']"
            },
            {
                "name": "Shimmer",
                "year": 1997,
                "artists": "['Fuel']"
            },
            {
                "name": "Symphony Of Destruction",
                "year": 1992,
                "artists": "['Megadeth']"
            },
            {
                "name": "Breaking the Habit",
                "year": 2003,
                "artists": "['Linkin Park']"
            },
            {
                "name": "Lovers Rock",
                "year": 2014,
                "artists": "['TV Girl']"
            },
            {
                "name": "Fell On Black Days",
                "year": 1994,
                "artists": "['Soundgarden']"
            },
            {
                "name": "New Divide",
                "year": 2009,
                "artists": "['Linkin Park']"
            },
            {
                "name": "War of Change",
                "year": 2012,
                "artists": "['Thousand Foot Krutch']"
            },
            {
                "name": "Freak",
                "year": 1997,
                "artists": "['Silverchair']"
            }
        ]
    }


def test_comic():
    response = client.post(
        "/comic",
        json={"comic": "Iron Man"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            "A Year of Marvels: August Infinite Comic (2016)",
            "A Year of Marvels: July Infinite Comic (2016)",
            "A Year of Marvels: June Infinite Comic (2016)",
            "A Year of Marvels: March Infinite Comic (2016)",
            "A Year of Marvels: May Infinite Comic (2016)",
            "A Year of Marvels: November Infinite Comic (2016)",
            "A Year of Marvels: October Infinite Comic (2016)",
            "A Year of Marvels: September Infinite Comic (2016)",
            "A Year of Marvels: The Amazing (2016)",
            "A Year of Marvels: The Incredible (2016)",
            "A+X (2012 - 2014)",
            "A+X (2012 - 2014)",
            "A+X (2012 - 2014)",
            "A+X (2012 - 2014)",
            "A+X (2012 - 2014)"
        ]
    }
