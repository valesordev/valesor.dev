package targets

import (
	"bytes"
	"net/http"
	"testing"
)

func TestReadDataTargetFromRequest(t *testing.T) {
	jsonStr := []byte(`{"metadata": {
        "apple":  "A sweet red or green fruit",
        "banana": "A long yellow fruit",
        "cherry": "A small, round, red fruit",
    }, "location": "somewhere", "interval": "daily", "format": "json"}`)
	req, err := http.NewRequest("POST", "/example", bytes.NewBuffer(jsonStr))
	if err != nil {
		t.Fatal(err)
	}

	obj, err := ReadDataTargetFromRequest(req)
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}

	expected := &DataTarget{
		Metadata: map[string]string{
			"apple":  "A sweet red or green fruit",
			"banana": "A long yellow fruit",
			"cherry": "A small, round, red fruit",
		},
		Location: "somewhere",
		Interval: 1,
		Format:   JSON,
	}

	if obj.Metadata["apple"] != expected.Metadata["apple"] || obj.Location != expected.Location || obj.Interval != expected.Interval || obj.Format != expected.Format {
		t.Errorf("Expected %v, got %v", expected, obj)
	}
}
