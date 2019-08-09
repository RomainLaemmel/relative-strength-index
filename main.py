import matplotlib.pyplot as plt
import relative_strength_index

def main():
    # Load a price series from file
    series = []
    with open('cac40_2018.txt') as f:
        content = f.read().splitlines()
    for i in content:
        series.append(float(i))

    # Compute RSI with a period of 14
    rsi = relative_strength_index.RSI(14)
    rsi_array = rsi.compute_rsi(series)

    # Display chart
    print(rsi_array)
    plt.plot(rsi_array)
    plt.ylim(0, 100)
    plt.grid()
    plt.margins(0)
    plt.axhspan(30, 70, facecolor='yellow', alpha=0.5)
    plt.title("Relative Strength Index")
    plt.show()

if (__name__ == '__main__'):
    main()