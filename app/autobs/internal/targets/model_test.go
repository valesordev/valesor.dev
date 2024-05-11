import (
	"bytes"
	"net/http"
	"net/http/httptest"
	"testing"
)

func TestReadJSONObjectFromRequest(t *testing.T) {
	jsonStr := []byte(`{"metadata": "example", "location": "somewhere", "interval": "daily", "format": "json"}`)
	req, err := http.NewRequest("POST", "/example", bytes.NewBuffer(jsonStr))
	if err != nil {
		t.Fatal(err)
	}

	obj, err := ReadJSONObjectFromRequest(req)
	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}

	expected := &MyJSONObject{
		Metadata: "example",
		Location: "somewhere",
		Interval: "daily",
		Format: "json",
	}

	if obj.Metadata != expected.Metadata || obj.Location != expected.Location || obj.Interval != expected.Interval || obj.Format != expected.Format {
		t.Errorf("Expected %v, got %v", expected, obj)
	}
}