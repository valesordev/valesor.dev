# Go parameters
GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOTEST=$(GOCMD) test
GOGET=$(GOCMD) get
PACKAGE_NAMESPACE=ghcr.com/valesordev/valesor.dev
BINARY_NAME=autobs
BINARY_UNIX=$(BINARY_NAME)_unix

all: test build
build: 
	$(GOBUILD) -o $(BINARY_NAME) -v ./cmd
test: 
	$(GOTEST) -v ./...
clean: 
	$(GOCLEAN)
	rm -f $(BINARY_NAME)
	rm -f $(BINARY_UNIX)
run:
	$(GOBUILD) -o $(BINARY_NAME) -v ./cmd
	./$(BINARY_NAME)
deps:
	$(GOGET) ./...
# Cross compilation
build-linux:
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 $(GOBUILD) -o $(BINARY_UNIX) -v ./cmd
docker-build:
	docker build -t $(PACKAGE_NAMESPACE)/$(BINARY_NAME) .

.PHONY: proto
proto:
    protoc -I api/protobuf/ api/protobuf/**/*.proto --go_out=plugins=grpc:internal/api
