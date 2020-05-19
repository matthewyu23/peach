import requests
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

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
        xAxis = []
        yAxis = []
        for report in c[0]["financials"]:
            xAxis.append(report["date"])
            if report["Revenue"] != "":
                yAxis.append(float(report["Revenue"]))
            else:
                yAxis.append(0)
        print(xAxis, yAxis)
        axs[i].xaxis.set_major_locator(plticker.MultipleLocator(base=len(xAxis)/5))
        axs[i].plot(xAxis, yAxis)
        i = i + 1
    plt.show()

if __name__ == "__main__":
    main()
