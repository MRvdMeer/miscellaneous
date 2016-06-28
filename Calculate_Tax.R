calculate.tax <- function(income = 0){
    cutoff.points <- c(19922, 33715, 66421)
    tax.rates <- c(0.3655, 0.4015, 0.4015, 0.52)
    tax <- min(income, cutoff.points[1]) * tax.rates[1] # first tax bucketbucket
    
    # iterate through all the other tax buckets
    for(i in 1:length(cutoff.points)-1){ 
        tax <- tax + min(max(0, income - cutoff.points[i]), cutoff.points[i+1] - cutoff.points[i]) * tax.rates[i+1]
    }
    c(tax = tax, net.income = income - tax, monthly.income = (income - tax) / 12)
}
