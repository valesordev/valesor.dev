# Step 1: Build the executable
# Use the official Golang image to create a build artifact.
# This is the build stage, where we use a heavier image with all the build tools necessary.
FROM golang:1.22.2 as builder

# Set the Current Working Directory inside the container
WORKDIR /app

# Copy go mod and sum files
COPY go.mod go.sum ./

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Copy the source code into the container
COPY . .

# Build the Go app
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o autobs ./cmd/autobs

# Step 2: Use a Docker multi-stage build to create a lean production image.
# Use a smaller image to run the application
FROM alpine:latest

LABEL org.opencontainers.image.source=https://github.com/valesordev/valesor.dev
LABEL org.opencontainers.image.description="Automated Observer"

# Set the Current Working Directory inside the container
WORKDIR /root/

# Import the user and group files from the builder.
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group

# Copy the Pre-built binary file from the previous stage
COPY --from=builder /app/autobs .

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the executable
CMD ["./autobs"]
