from src.functional import formation


def test_formation() -> None:
    s3 = 'Sokrat is teacher of Platon'
    t1 = formation('Hello, {}', 'Vasya') == 'Hello, Vasya'
    t2 = formation('Franz {}', 'Kafka') == 'Franz Kafka'
    t3 = formation('Sokrat is teacher of {}', 'Platon') == s3
    assert t1
    assert t2
    assert t3
