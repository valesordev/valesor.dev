package targets

import (
	"encoding/json"
	"net/http"
)

func ReadDataTargetFromRequest(r *http.Request) (*DataTarget, error) {
	var obj MyJSONObject
	err := json.NewDecoder(r.Body).Decode(&obj)
	if err != nil {
		return nil, err
	}
	return &obj, nil
}
type DataTarget struct {
	Metadata  string `json:"metadata"`
	Location  string `json:"location"`
	Interval  string `json:"interval"`
	Format   string `json:"format"`
}
