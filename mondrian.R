# generates random Mondrian-style drawing

draw.rectangle <- function(nrect = 1, n.seed = 1){
  set.seed(n.seed)
  all_colors <- colors(distinct = TRUE)
  plot(c(0, 100), c(0, 100), type = "n", xaxt = "n", yaxt = "n", pty = "s")
  xleftcorners <- sample(0:100, nrect, replace = TRUE)
  xrightcorners <- sample(0:100, nrect, replace = TRUE)
  yleftcorners <- sample(0:100, nrect, replace = TRUE)
  yrightcorners <- sample(0:100, nrect, replace = TRUE)
  colors = sample(length(all_colors), nrect)
  rect(xleftcorners, xrightcorners, yleftcorners, yrightcorners, col = all_colors[colors])
}
