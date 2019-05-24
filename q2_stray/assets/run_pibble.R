#!/usr/bin/env Rscript

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

# TODO: add an option for phylogenetic prior
# no phylogenetic prior
m <- rowMeans(alr_array(Y+0.65, parts=1))
upsilon <- D-1+3
Theta <- matrix(0, D-1, N)
Theta[] <- m
Xi <- matrix(.4, D-1, D-1)
diag(Xi) <- 1
Gamma <- diag(nrow(X))

fit <- pibble(Y, diag(N), upsilon, Theta, Gamma, Xi)
fit_lambda <- summary(fit, pars="Lambda")$Lambda
posterior <- pibble_tidy_samples(fit)

write.csv(fit_lambda, out.differential)
write.csv(posterior, out.posterior)
