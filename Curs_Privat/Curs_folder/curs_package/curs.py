# https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5
import requests


class ApiClient:
    def __init__(self, fetch: requests):
        self.fetch = fetch

    def get_json(self, url):
        response = self.fetch.get(url)
        return response.json()


def main(data: list[dict]):
    pattern = "|{:^10}|{:^10}|{:^10}"
    print(pattern.format("currency", "sale", "buy"))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get("buy")
        sale = el.get(currency).get("sale")
        print(pattern.format(currency, sale, buy))


def adapter_result(data):
    return [
        {
            f"{el.get('ccy')}": {
                "buy": float(el.get("buy")),
                "sale": float(el.get("sale")),
            }
        }
        for el in data
    ]


if __name__ == "__main__":
    client = ApiClient(requests)
    data = client.get_json(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )

    main(adapter_result(data))
   
