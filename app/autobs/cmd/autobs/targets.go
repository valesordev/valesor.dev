package autobs

import (
	"github.com/spf13/cobra"
)

var targetCmd = &cobra.Command{
	Use:   "target",
	Short: "Manage observation targets",
	Long:  `The target command allows you to upsert, delete, list, serve, and record observation targets.`,
}

var upsertCmd = &cobra.Command{
	Use:   "upsert",
	Short: "Upsert an observation target",
	Long:  `The upsert command allows you to upsert an observation target.`,
}

var deleteCmd = &cobra.Command{
	Use:   "delete",
	Short: "Delete an observation target",
	Long:  `The delete command allows you to delete an observation target.`,
}

var listCmd = &cobra.Command{
	Use:   "list",
	Short: "List observation targets",
	Long:  `The list command allows you to list observation targets.`,
}

var serveCmd = &cobra.Command{
	Use:   "serve",
	Short: "Serve observation targets",
	Long:  `The serve command allows you to serve observation targets.`,
}

var recordCmd = &cobra.Command{
	Use:   "record",
	Short: "Record observation targets",
	Long:  `The record command allows you to record observation targets.`,
}

func init() {
	upsertCmd.Flags.Stringp("name", "n", "", "Name of the target")
	upsertCmd.Flags.Stringp("uri", "u", "", "URI of the target")
	targetCmd.AddCommand(upsertCmd)
	deleteCmd.Flags.Stringp("name", "n", "", "Name of the target")
	targetCmd.AddCommand(deleteCmd)
	targetCmd.AddCommand(listCmd)
	targetCmd.AddCommand(serveCmd)
	recordCmd.Flags.Stringp("records", "r", "", "Path to the records file")
	targetCmd.AddCommand(recordCmd)

	// Initialize other sub-commands here, similarly
}
