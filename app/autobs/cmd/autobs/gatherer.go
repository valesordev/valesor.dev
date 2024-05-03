package autobs

import (
	"github.com/spf13/cobra"
)

var gathererCmd = &cobra.Command{
	Use:   "gatherer",
	Short: "Control and manage gatherers",
	Long:  `The gatherer command allows you to run, validate, and serve_metrics for gatherers.`,
}

var runCmd = &cobra.Command{
	Use:   "run",
	Short: "Run a gatherer",
	Long:  `The run command allows you to run a gatherer.`,
}

var validateCmd = &cobra.Command{
	Use:   "validate",
	Short: "Validate a gatherer",
	Long:  `The validate command allows you to validate a gatherer.`,
}

var serveMetricsCmd = &cobra.Command{
	Use:   "serve_metrics",
	Short: "Serve metrics for a gatherer",
	Long:  `The serve_metrics command allows you to serve metrics for a gatherer.`,
}

func init() {
	gathererCmd.AddCommand(runCmd)
	gathererCmd.AddCommand(validateCmd)
	gathererCmd.AddCommand(serveMetricsCmd)

	// Initialize other sub-commands here, similarly
}
