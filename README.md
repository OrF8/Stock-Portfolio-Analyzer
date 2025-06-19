# 📊 Stock-Portfolio-Analyzer
A lightweight Python script designed to analyze stock portfolios by calculating key financial metrics such as volatility and beta relative to a benchmark index.

## 🔍 Features
- **Portfolio Volatility**: Calculates both daily and annualized volatility of your portfolio.
- **Benchmark Volatility**: Computes the volatility metrics for a specified benchmark index.
- **Beta Calculation**: Determines the portfolio's beta relative to the benchmark, indicating the portfolio's sensitivity to market movements.

## 🚀 Getting Started
### Running locally
#### Prerequisites
- Python 3.x (preferably 3.9)
- Recommended: Use a virtual environment to manage dependencies
#### Installation
1. Clone the repository:
   ````bash
   git clone https://github.com/OrF8/Stock-Portfolio-Analyzer.git
   cd Stock-Portfolio-Analyzer
   ````
2. Set up a virtual environment:
   ````bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ````
3. install the required packages:
   ````bash
   pip install -r requirements.txt
   ````

#### 📈 Usage
1. Ensure your portfolio and benchmark data are prepared in the appropriate format.
2. Run the analysis script:
   ````bash
   python portfolio_analyzer.py
   ````
3. Follow the on-screen prompts to input your data files and view the calculated metrics.

### 📦 Using GitHub Codespaces or Dev Containers
This project supports [**GitHub Codespaces**](https://github.com/features/codespaces) and [**VS Code Dev Containers**](https://code.visualstudio.com/docs/devcontainers/containers).  
A preconfigured development environment is available via the `.devcontainer` folder.

To get started:

- If you're using **Codespaces**, click the **"Code"** button on the repository and choose **"Create codespace on main"**.
- If you're using **VS Code with Dev Containers** locally:
  1. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
  2. Open the project in VS Code.
  3. Run `Dev Containers: Reopen in Container` from the command palette.

The container automatically installs all required Python packages listed in `requirements.txt`.

## 📊 Example
Sample data is provided in the `example_data/` directory to demonstrate the script's functionality.

## 🗂️ Project Structure
````
Stock-Portfolio-Analyzer/
├── .devcontainer/          # Dev. container configuration for github codespaces
│   ├── devcontainer.json   # Configuration file for the dev container
│   └── postCreate.sh       # Script to run after the container is created
├── example_data/           # Sample data files for demonstration
├── portfolio_analyzer.py   # Main script for analysis
├── requirements.txt        # Python dependencies
├── Portfolio Analyzer.zip  # Zipped version of the project
├── .gitattributes          # Git attributes configuration
├── LICENSE                 # MIT License
└── README.md               # Project documentation, you are here!
````

# 📄 License
This project is licensed under the MIT License – see the [**LICENSE**](https://github.com/OrF8/Stock-Portfolio-Analyzer/blob/main/LICENSE) file for details.
