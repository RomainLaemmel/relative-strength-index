class RSI:

    def __init__(self, period):
        self.period = period
        self.prev_avg_gain = 0
        self.prev_avg_loss = 0
        self.rsi = []

    def compute_moving_average(self, series):
        if len(self.rsi) == 0:
            sum_gain = 0
            sum_loss = 0
            for v1, v2 in zip(series[:-1], series[1:]):
                if v2 > v1:
                    sum_gain += v2 - v1
                elif v1 > v2:
                    sum_loss += v1 - v2
            avg_gain = sum_gain / self.period
            avg_loss = sum_loss / self.period
        else:
            if series[-1] >= series[-2]:
                gain = series[-1] - series[-2]
                loss = 0
            elif series[-2] > series[-1]:
                gain = 0
                loss = series[-2] - series[-1]
            avg_gain = (gain + ((self.period - 1) * self.prev_avg_gain)) / self.period
            avg_loss = (loss + ((self.period - 1) * self.prev_avg_loss)) / self.period
        self.prev_avg_gain = avg_gain
        self.prev_avg_loss = avg_loss
        return avg_gain, avg_loss

    def compute_single_rsi(self, series):
        avg_gain, avg_loss = self.compute_moving_average(series)
        if avg_loss == 0:
            rsi = 100
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))
        return rsi

    def compute_rsi(self, series):
        self.rsi = []
        for i in range(self.period, len(series)):
            self.rsi.append(self.compute_single_rsi(series[i - self.period:i + 1]))
        return self.rsi