from datetime import datetime, timedelta
from models.Card import Card
import math
import pytest
import time


def test_create_card():
    newCard = Card(
        word='Banana',
        definition='Seriously?...its the worlds most popular fruit!'
    )

    # a new card at 0 should still move to bucket 1 when marked wrong
    newCard.mark_wrong()
    assert newCard.bucket == 1

    # a card in bucket 1 should not drop below 1
    newCard.mark_wrong()
    assert newCard.bucket == 1

    cardAvailable = (datetime.now() + timedelta(seconds=5)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    # every wrong answer should count
    assert newCard.wrong_count == 2

    newCard.mark_right()
    assert newCard.bucket == 2
    cardAvailable = (datetime.now() + timedelta(seconds=25)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    newCard.mark_right()
    assert newCard.bucket == 3
    cardAvailable = (datetime.now() + timedelta(minutes=2)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    newCard.mark_right()
    assert newCard.bucket == 4
    cardAvailable = (datetime.now() + timedelta(minutes=10)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    newCard.mark_right()
    assert newCard.bucket == 5
    cardAvailable = (datetime.now() + timedelta(hours=1)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    # marking the card right should not add to the wrong count
    assert newCard.wrong_count == 2

    newCard.mark_right()
    assert newCard.bucket == 6
    cardAvailable = (datetime.now() + timedelta(hours=5)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    newCard.mark_wrong()
    assert newCard.bucket == 5
    cardAvailable = (datetime.now() + timedelta(hours=1)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)
    assert newCard.wrong_count == 3

    newCard.mark_right()
    assert newCard.bucket == 6
    cardAvailable = (datetime.now() + timedelta(hours=5)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    newCard.mark_right()
    assert newCard.bucket == 7
    cardAvailable = (datetime.now() + timedelta(days=1)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    newCard.mark_right()
    assert newCard.bucket == 8
    cardAvailable = (datetime.now() + timedelta(days=5)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    newCard.mark_right()
    assert newCard.bucket == 9
    cardAvailable = (datetime.now() + timedelta(days=25)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    newCard.mark_right()
    assert newCard.bucket == 10
    cardAvailable = (datetime.now() + timedelta(days=121)).timestamp()
    assert newCard.available.timestamp() == pytest.approx(cardAvailable)

    newCard.mark_right()
    assert newCard.bucket == 11
    daysInOneHundredAndFiftyYears = math.floor(365.4 * 150)
    cardStillNotAvailable = (
        datetime.now() + timedelta(days=daysInOneHundredAndFiftyYears)).timestamp()
    assert newCard.available.timestamp() > cardStillNotAvailable

    # a card should never go higher than bucket 11 even if a user manages to mark it
    # right when its in bucket 11 (should actually never be seen)
    newCard.mark_right()
    assert newCard.bucket == 11

    newCard.mark_right()
    newCard.mark_right()
    newCard.mark_right()
    newCard.mark_right()
    newCard.mark_right()
    assert newCard.bucket == 11
