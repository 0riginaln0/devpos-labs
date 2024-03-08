# https://github.com/nodejs/docker-node/
# build stage
FROM debian:12 as builder
RUN apt-get update -y
RUN apt-get install -y \
    llvm-dev \
    clang \
    git 
RUN git clone https://github.com/odin-lang/Odin
#RUN git checkout master
WORKDIR Odin
RUN ./build_odin.sh
WORKDIR ..

# actual odin image
FROM debian:12 as odin_debian
RUN apt-get update -y
RUN apt-get install clang -y
RUN mkdir /Odin
COPY --from=builder /Odin/vendor /Odin/vendor
COPY --from=builder /Odin/shared /Odin/shared
COPY --from=builder /Odin/odin /Odin/odin
COPY --from=builder /Odin/examples /Odin/examples
COPY --from=builder /Odin/core /Odin/core
COPY --from=builder /Odin/base /Odin/base
ENV PATH $PATH:/Odin
RUN mkdir /app
COPY /one_two_three /app/one_two_three
WORKDIR app
CMD [ "odin", "run", "one_two_three"]