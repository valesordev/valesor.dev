package gatherer

import (
	"net/http"

	"github.com/spf13/cobra"
)

func RunCommand(cmd *cobra.Command, args []string) {
	client := &http.Client{}
	resp, err := client.Get("http://localhost:8080")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
}
