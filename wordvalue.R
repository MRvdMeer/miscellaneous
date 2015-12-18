# compute letter values of each word
# determine if the value is exactly 100
# if so, save in an array and print

filepath <- "OpenTaal-210G-basis-gekeurd.txt"

compute.value <- function(word){
  if(!is.character(word)){stop("not a word")}
  if(length(word) > 1){stop("enter only one word")}
  word.letters <- strsplit(tolower(word), split = "")[[1]]
  sum(match(word.letters, letters), na.rm = FALSE)
}

word.list <- read.delim(file = filepath, header = FALSE, stringsAsFactors = FALSE)[, 1]
value.words <- NULL

for(word in word.list){
  x <- compute.value(word)
  if(is.na(x)){next}
  if(x == 100){
    value.words <- c(value.words, word)
  }
}

sort(tolower(value.words))
