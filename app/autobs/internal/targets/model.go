package targets

import (
	"encoding/json"
	"net/http"
)

func ReadDataTargetFromRequest(r *http.Request) (*DataTarget, error) {
	var obj DataTarget
	err := json.NewDecoder(r.Body).Decode(&obj)
	if err != nil {
		return nil, err
	}
	return &obj, nil
}

type DataFormat int

const (
	JSON DataFormat = iota
	XML
)

type DataTarget struct {
	Metadata map[string]string `json:"metadata"`
	Location string            `json:"location"`
	Interval uint8             `json:"interval"`
	Format   DataFormat        `json:"format"`
}

type DataSnapshot struct {
	Metadata  map[string]string `json:"metadata"`
	RawData   string            `json:"data"`
	Timestamp int64             `json:"timestamp"`
	Target    *DataTarget       `json:"target"`
}
