# lb4anyatvbox

"lb4anyatvbox" is a Python tool that allows you to make and build custom logos on any Android TV device.

## 1. Setup

### Prerequisites

- Python 3.8 or newer
- Git

> You will also need the following system packages depending on your OS.

#### Ubuntu / Debian

```sh
sudo apt update
sudo apt install python3 python3-pip git
```

#### Arch Linux / Manjaro

```sh
sudo pacman -Syu python python-pip git
```

#### macOS (with Homebrew)

```sh
brew install python git
```

### Clone the Repository

```sh
git clone https://github.com/SharkZubat/lb4anyatvbox.git
cd lb4anyatvbox
```

### Install Python Dependencies

```sh
pip install -r requirements.txt
```

## 2. Usage

To start the tool, run:

```sh
./lbatv
```

If you encounter a "Permission denied" error, make the script executable:

```sh
chmod +x lbatv
./lbatv
```

## 3. Next Steps

- Follow the on-screen instructions provided by the tool.
- For advanced configuration, check for a `config` or `.env` file in the repository (if provided).
- If you face issues, please open an issue on the [GitHub repository](https://github.com/SharkZubat/lb4anyatvbox/issues).

---

Feel free to contribute or suggest improvements!
