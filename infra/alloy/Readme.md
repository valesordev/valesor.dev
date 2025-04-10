# Alloy development and testing

Running with Docker:

    docker run --name=grafana-alloy --rm \
      -v ./testing/csv_file.alloy:/etc/grafana/config.alloy \
      -v ./testing/random_data.csv:/data/random_data.csv \
      -p 12346:12345 \
      grafana/alloy run /etc/grafana/config.alloy
