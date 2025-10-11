# Espanso App-Specific Configurations

This directory contains app-specific configurations for espanso that are git-tracked as part of the heme-texts project.

## Current Configurations

### Citrix Configuration (`citrix.yml`)

This configuration is specifically designed for the Citrix Hyperspace FHCC PATHOLOGY environment to address text replacement issues commonly encountered in virtualized applications.

**Key features:**
- Uses clipboard backend for better compatibility with Citrix
- Increased delays to prevent first letter omission/overwriting
- Disabled word boundaries for better matching
- Conservative text replacement approach

**Detection criteria:**
- `filter_exec`: "Citrix Viewer.app"
- `filter_title`: "Hyperspace.*FHCC PATHOLOGY"

## Setup

To set up the espanso configurations:

```bash
# Run the setup script
python scripts/setup_espanso_configs.py

# Restart espanso to apply changes
espanso restart
```

## Manual Setup

If you prefer to set up manually:

```bash
# Create symlinks for each config file
ln -sf /Users/christophersnyder/Projects/heme-texts/espanso-configs/citrix.yml ~/.config/espanso/config/citrix.yml
```

## Troubleshooting

### First Letter Issues in Citrix

The Citrix configuration addresses common text replacement issues by:

1. **Using Clipboard Backend**: More reliable than direct injection in virtualized environments
2. **Increased Delays**: Prevents race conditions that cause first letter issues
3. **Disabled Word Boundaries**: Allows matches to work even with partial word contexts
4. **Conservative Timing**: Extra delays around paste operations

### Testing Configuration

To test if the configuration is active:

1. Open the Citrix application
2. Type `#detect#` to see current app information
3. Type `#acfg#` to see the active configuration
4. Test your text replacements

### Common Issues

- **Configuration not loading**: Ensure espanso is restarted after changes
- **Symlinks not working**: Check that the source files exist and paths are correct
- **Still having first letter issues**: Try increasing the delay values in the config

## Adding New Configurations

To add a new app-specific configuration:

1. Create a new `.yml` file in this directory
2. Add the filename to `config_files` in `scripts/setup_espanso_configs.py`
3. Run the setup script
4. Test the configuration

## Configuration Options

For a complete list of available configuration options, see the [espanso documentation](https://espanso.org/docs/configuration/options/).
