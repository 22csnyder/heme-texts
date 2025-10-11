# Shell Execution Test

This file demonstrates the espanso shell execution functionality.

## Test Commands

Here are the test commands from your notepad:

```txt
```sh cd ~; ls ```
```


## Additional Test Commands

```sh
pwd
```

```sh
echo "Hello from espanso shell execution!"
```

```sh
date
```

```sh
whoami
```

## Instructions

1. Type the commands above in any text editor
2. The espanso trigger should automatically execute the shell commands and replace them with the output
3. The regex pattern matches ```sh followed by any content and ending with ```

## Expected Behavior

- ````sh cd ~; ls ```` should execute the command and show your home directory contents
- ````sh pwd ```` should show the current working directory
- ````sh echo "Hello from espanso shell execution!" ```` should display the echo message
