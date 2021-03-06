FROM golang:1.15

WORKDIR /go/src/manager

COPY manager.go .

RUN go get -v ./...
RUN go install -v ./...

CMD ["manager"]
