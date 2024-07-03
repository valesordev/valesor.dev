package targets

import (
	"github.com/spf13/cobra"
)

func RunUpsertCommand(cmd *cobra.Command, args []string, location string, interval uint8, format bool, metadata map[string]string) {
}

func RunDeleteCommand(cmd *cobra.Command, args []string, location string) {
}

func RunListCommand(cmd *cobra.Command, args []string) {
}

func RunServeCommand(cmd *cobra.Command, args []string) {
}

func RunRecordCommand(cmd *cobra.Command, args []string, recordsPath string, location string, metadata map[string]string) {
}
