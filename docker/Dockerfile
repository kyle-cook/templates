# Using alpine base
FROM alpine

# Image for base ruby environment
MAINTAINER kyle-cook@utulsa.edu

# Update and Upgrade
RUN apk update && apk upgrade

# Give ourselves a non-root user
USER anonymous
WORKDIR /home/anonymous
