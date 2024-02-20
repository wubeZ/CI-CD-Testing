from fizzbuzz import solve


def test_on_fizzbuzz():
    assert solve(3) == "Fizz"
    assert solve(5) == "Buzz"
    assert solve(15) == "FizzBuzz"
    assert solve(1) == 1