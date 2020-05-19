import requests
import json
import matplotlib.pyplot as plt

def recieve_data():
    tickers = input("ticker: ").split()
    print(tickers)
    all_data = []
    for t in tickers:
        temp = []
        income_template = f"https://financialmodelingprep.com/api/v3/financials/income-statement/{t}?period=quarter"
        balance_template = f"https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/{t}?period=quarter"
        cashflow_template = f"https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/{t}?period=quarter"
        temp.append(requests.get(income_template).json())
        temp.append(requests.get(balance_template).json())
        temp.append(requests.get(cashflow_template).json())
        all_data.append(temp)
    return all_data


def main():
    all_data = recieve_data()
    print(len(all_data))
    i = 0
    fig, axs = plt.subplots(1, len(all_data))
    print(axs)
    for c in all_data:
        axs[i].set_title(c[0]["symbol"])
        axs[i].plot([1, 2, 3], [1, 2, 3])
        i = i + 1
    plt.show()

if __name__ == "__main__":
    main()
