from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_movie():
    response = client.post("/movie", json={"movie": "Toy Story"})
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
            "Toy Story Toons: Hawaiian Vacation (2011)",
        ]
    }


def test_anime():
    response = client.post("/anime", json={"movie": "Death Note"})
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
            "Kara no Kyoukai 4: Garan no Dou",
        ]
    }


def test_book():
    response = client.post("/anime", json={"book": "1984"})
    assert response.status_code == 200


def test_game():
    response = client.post("/game", json={"game": "Call of Duty"})
    assert response.status_code == 200


def test_manga():
    response = client.post("/manga", json={"manga": "Otona No Mondai"})
    assert response.status_code == 200


def test_music_bad():
    response = client.post(
        "/songs",
        json={"music": [{"name": "Come As You Are", "year": 1991}]},
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "songs"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_music_good():
    response = client.post(
        "/songs",
        json={
            "songs": [
                {"name": "Come As You Are", "year": 1991},
                {"name": "The Sign", "year": 1994},
            ]
        },
    )
    assert response.status_code == 200


def test_comic():
    response = client.post("/comic", json={"comic": "Iron Man"})
    assert response.status_code == 200
