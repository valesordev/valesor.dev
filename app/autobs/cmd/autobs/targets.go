package autobs

import (
	"github.com/valesordev/autobs/internal/targets"

	"github.com/spf13/cobra"
)

var location string
var interval uint8
var format bool
var metadata map[string]string
var recordsPath string

var targetCmd = &cobra.Command{
	Use:   "target",
	Short: "Manage observation targets",
	Long:  `The target command allows you to upsert, delete, list, serve, and record observation targets.`,
}

var upsertCmd = &cobra.Command{
	Use:   "upsert",
	Short: "Upsert an observation target",
	Long:  `The upsert command allows you to upsert an observation target.`,
	Run: func(cmd *cobra.Command, args []string) {
		targets.RunUpsertCommand(cmd, args, location, interval, format, metadata)
	},
}

var deleteCmd = &cobra.Command{
	Use:   "delete",
	Short: "Delete an observation target",
	Long:  `The delete command allows you to delete an observation target.`,
	Run: func(cmd *cobra.Command, args []string) {
		targets.RunDeleteCommand(cmd, args, location)
	},
}

var listCmd = &cobra.Command{
	Use:   "list",
	Short: "List observation targets",
	Long:  `The list command allows you to list observation targets.`,
	Run: func(cmd *cobra.Command, args []string) {
		targets.RunListCommand(cmd, args)
	},
}

var serveCmd = &cobra.Command{
	Use:   "serve",
	Short: "Serve observation targets",
	Long:  `The serve command allows you to serve observation targets.`,
	Run: func(cmd *cobra.Command, args []string) {
		targets.RunServeCommand(cmd, args)
	},
}

var recordCmd = &cobra.Command{
	Use:   "record",
	Short: "Record observation targets",
	Long:  `The record command allows you to record observation targets.`,
	Run: func(cmd *cobra.Command, args []string) {
		targets.RunRecordCommand(cmd, args, recordsPath, location, metadata)
	},
}

func init() {
	upsertCmd.Flags().StringVar(&location, "location", "", "Location of the target")
	upsertCmd.Flags().Uint8Var(&interval, "interval", 1, "How oftent to run this target")
	upsertCmd.Flags().BoolVar(&format, "format", false, "Is this json")
	upsertCmd.Flags().StringToStringVar(&metadata, "metadata", nil, "Metadata of the target")

	deleteCmd.Flags().StringVar(&location, "location", "", "Location of the target")

	recordCmd.Flags().StringVar(&recordsPath, "records", "", "Path to the records file")
	recordCmd.Flags().StringVar(&location, "location", "", "Location of the target")
	recordCmd.Flags().StringToStringVar(&metadata, "metadata", nil, "Metadata of the target")

	targetCmd.AddCommand(upsertCmd)
	targetCmd.AddCommand(deleteCmd)
	targetCmd.AddCommand(listCmd)
	targetCmd.AddCommand(recordCmd)
	targetCmd.AddCommand(serveCmd)
}
