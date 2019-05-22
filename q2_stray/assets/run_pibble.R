library(phyloseq)
library(stray)
library(dplyr)
library(ape)
library(driver)


args <- commandArgs(TRUE)
inp.abundances.path <- args[[1]]
inp.metadata.path <- args[[2]]
formula <- args[[3]]
learning_rate <- args[[4]]
beta1 <- args[[5]]
beta2 <- args[[6]]

out.differential <- args[[4]]
out.posterior <- args[[5]]

map <- read.csv(inp.metadata.path, row.names=1, header = TRUE)
dat <- read.delim(inp.abundances.path, row.names=1, skip = 1, comment.char='')

X <- t(model.matrix(paste("~", formula), data=map))
Y <- otu_table(dat)

ntaxa = dim(otu)[1]

upsilon <- ntaxa(dat)+3
m <- diag(ntaxa(dat)) + 0.5*vcv.phylo(phy_tree(dat), corr=TRUE) # Weak Phylo Prior
GG <- cbind(diag(ntaxa(dat)-1), -1)
Xi <- (upsilon-ntaxa(dat)-2)*GG%*%m%*%t(GG)
Theta <- matrix(0, ntaxa(dat)-1, nrow(X))
Gamma <- diag(nrow(X))

priors <- pibble(NULL, X, upsilon, Theta, Gamma, Xi)

priors$Y <- Y # add data to priors object
Xi <- (upsilon-ntaxa(dat)-2)*GG%*% diag(ntaxa(dat)) %*%t(GG) # update Xi prior
Xi_clr <- driver::alrvar2clrvar(Xi, ntaxa(dat)) # need to add it in CLR coords
priors$Xi <- Xi_clr # add new prior to mongrelfit object
verify(priors) # run internal checks to make sure modified object is okay


fit <- refit(priors, step_size=0.005, b1=beta1, b2=beta2, decomp_method="cholesky")
fit_lambda <- summary(fit, pars="Lambda")$Lambda
posterior <- pibble_tidy_samples(fit)

write.csv(fit_lambda, out.differential)
write.csv(posterior, out.posterior)
