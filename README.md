# DeltaGuard

DeltaGuard is a Python program designed to enhance workspace organization and accessibility by creating and managing multiple virtual desktops on Windows. It allows users to create, switch, and manage virtual desktops to streamline their workflow and improve productivity.

## Features

- **Create Virtual Desktops:** Easily create new virtual desktops to organize your workspace.
- **Switch Desktops:** Switch between different virtual desktops seamlessly.
- **Move Windows:** Move specific application windows between virtual desktops.
- **List Windows:** List all open windows on the current virtual desktop.
- **Close Desktops:** Close virtual desktops when they are no longer needed.

## Requirements

- Python 3.x
- Windows operating system
- Required Python packages: `pygetwindow`, `pywinauto`

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Install the required Python packages using pip:

   ```bash
   pip install pygetwindow pywinauto
   ```

3. Download the `deltaguard.py` file from this repository.

## Usage

Run the `deltaguard.py` script using Python:

```bash
python deltaguard.py
```

Follow the on-screen instructions to create and manage virtual desktops.

## Limitations

- This program is designed to work only on Windows operating systems.
- Some functionality may require administrative privileges.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes or suggestions.

## Acknowledgments

DeltaGuard uses the `pygetwindow` and `pywinauto` libraries to interface with Windows' window management features.

---

Thank you for using DeltaGuard! We hope it enhances your productivity and workspace organization.