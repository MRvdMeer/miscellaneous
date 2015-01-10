## This file contains some functions to calculate mortgage payments given principal, interest, duration of the mortgage,
## and type of mortgage (either linear or annuity). The combo_mortgage function allows for a mortgage that is a combination
## of both linear and annuity-type mortgages.


mortgage <- function(type = "linear", principal = 0, interest = 5, months = 360){
  options(scipen=15,digits=10)
  ##interest is in % per year
  
  if(!(type %in% c("linear","annuity"))){
    stop("Invalid mortgage type")
  }
  interest_monthly <- interest/1200
  start_value <- principal
  int_payment <- NULL
  ending_value <- NULL
  total_payment <- NULL
  if(type == "linear"){
    prin_repayment <- principal/months
    for(i in 1:months){
      int_payment[i] <- start_value[i]*interest_monthly
      ending_value[i] <- start_value[i] - prin_repayment
      total_payment[i] <- prin_repayment + int_payment[i]
      start_value[i+1] <- ending_value[i]
    }
    start_value <- start_value[1:months]
  } else if(type == "annuity"){
    prin_repayment <- NULL
    dummy <- (1-(1+interest_monthly))/(1-((1+interest_monthly)^months))
    for(i in 1:months){
      int_payment[i] <- start_value[i]*interest_monthly
      prin_repayment[i] <- principal*dummy*((1+interest_monthly)^(i-1))
      ending_value[i] <- start_value[i] - prin_repayment[i]
      total_payment[i] <- prin_repayment[i] + int_payment[i]
      start_value[i+1] <- ending_value[i]
    }
    start_value <- start_value[1:months]
  }
  period <- 1:months
  output <- cbind(period, start_value, prin_repayment, int_payment, ending_value, total_payment)
  ##cat("Total Payment:",sum(output[,6]), "| Average Monthly Payment:",mean(output[,6]), "| Highest Monthly Payment:",max(output[,6]),"\n")
  return(output)
}

addMatrix <- function(matrix1,matrix2){
    ##coordinate-wise addition of matrix elements. 
    ##If the matrices are not of the same size, then it creates a matrix with number of rows and columns
    ##equal to the maximum between the two matrices and adds zeroes to the non-corresponding elements.
    rows1 <- nrow(matrix1)
    rows2 <- nrow(matrix2)
    cols1 <- ncol(matrix1)
    cols2 <- ncol(matrix2)
    
    rows <- max(rows1,rows2)
    cols <- max(cols1,cols2)
    output <- matrix(0,rows,cols)
    for(i in 1:rows){
        for(j in 1:cols){
            output[i,j] <- tryCatch(matrix1[i,j], error = function(e){return(0)}) + tryCatch(matrix2[i,j], error = function(e){return(0)})
        }
    }
    return(output)
}

combo_mortgage <- function(linearAmount = 0, linearInterest = 5, linearMonths = 360, annuityAmount = 0, annuityInterest = 5, annuityMonths = 360){
    ##interest is in % per year
    
    linearMortgage <- mortgage("linear", linearAmount, linearInterest, linearMonths)
    annuityMortgage <- mortgage("annuity", annuityAmount, annuityInterest, annuityMonths)
    output <- addMatrix(linearMortgage, annuityMortgage)
    colnames(output) <- c("Period","Start_Value","Prin_Repayment","Int_Payment","Ending_Value","Total_Payment")
    cat("Total Payment for Linear:",sum(linearMortgage[,6]), 
        "| Average Monthly Payment for Linear:",mean(linearMortgage[,6]), 
        "| Highest Monthly Payment for Linear:",max(linearMortgage[,6]),"\n")
    cat("Total Payment for Annuity:",sum(annuityMortgage[,6]), 
        "| Average Monthly Payment for Annuity:",mean(annuityMortgage[,6]), 
        "| Highest Monthly Payment for Annuity:",max(annuityMortgage[,6]),"\n")
    cat("Total Payment:",sum(output[,6]), 
        "| Average Monthly Payment:",mean(output[,6]), 
        "| Highest Monthly Payment:",max(output[,6]),"\n")
    return(output)
}