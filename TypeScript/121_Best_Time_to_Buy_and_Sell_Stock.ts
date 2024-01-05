function maxProfit(prices: number[]): number {
    let l = 0;
    let r = 1;
    let maxProfit = 0;

    while (r < prices.length) {
        if (prices[r] < prices[l]) {
            l = r;
        } else {
            maxProfit = Math.max(maxProfit, prices[r] - prices[l]);
        }
        r++;
    }

    return maxProfit;
};