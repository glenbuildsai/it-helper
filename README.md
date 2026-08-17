cat > README.md << 'EOF'
# IT Helper CLI

A command-line troubleshooting assistant powered by the Anthropic API. Ask plain-language IT questions and get step-by-step guidance from Claude.

## Features

- Interactive command-line interface
- Powered by Claude (Haiku) for fast, low-cost responses
- Simple, focused IT troubleshooting workflow

## Requirements

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com/settings/keys)

## Setup

1. Clone the repository:
```bash
   git clone https://github.com/YOUR_USERNAME/it-helper.git
   cd it-helper
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Add your API key. Create a `.env` file in the project root: