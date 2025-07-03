# Curis
Curis is a Streamlit AI platform with LLMs and an integrated robotic assistant for medical injury analysis. Upload injury images for automated diagnostics, treatment recommendations, and reports. The robot delivers real-time guidance and vocalizes insights. Powered by CrewAI, LangChain &amp; Google Generative A, Curis lets clinicians and researchers:

- **Injury Analysis:** Upload injury photos for image-based feature extraction, LLM-driven interpretation, and real-time feedback from the onboard robot.  
- **Treatment Recommendations:** Receive contextual drug prescriptions and care plans, which the robot can vocalize or display on its screen.  
- **Report Generation:** Produce polished, exportable PDFs summarizing findings, next steps, and robotic-guided instructions.

## 📂 Project Structure

\`\`\`
.
├── agents.py                  # Agent definitions (medical injury analyzer, QA, etc.)

├── tasks.py                   # Task workflows for injury analysis & report generation

├── pages/                     # Streamlit multipage app

│   ├── 1_injury-report.py     # Injury report page

│   ├── 2_drug-report.py       # Drug prescription report page

│   └── 3_final-report.py      # Final compiled report page

├── tools/                     # Utility modules

│   ├── tool_kit.py

│   └── vision_tool.

├── 3DOF Inverse Kinematic-PseudoInvJacobian

├── injury-report-analysis.md  # Markdown analysis of injury images

├── treatment_report.md        # Treatment insights report

├── requirements.txt           # Python dependencies

├── .gitignore                 # Files to ignore in Git

├── .env.local                 # Environment variables (API keys) – **gitignored**

├── keys.py                    # Loads API keys from .env.local

└── README.md                  # Project overview (this file)
\`\`\`

## 🚀 Installation

\`\`\`bash

python3 -m venv venv

source venv/bin/activate      # Linux/macOS

venv\\Scripts\\activate       # Windows

pip install --upgrade pip

pip install -r requirements.txt
\`\`\`

## 🔧 Configuration

Create a file named \`.env.local\` in the project root with your API keys:

\`\`\`bash
cat > .env.local << 'EOF'

SERPER_API_KEY=<your-serper-key>

GEMINI_API_KEY=<your-gemini-key>

OPENAI_API_KEY=<your-openai-key>

EOF
\`\`\`

## 🖥️ Running the App

\`\`\`bash
streamlit run pages/1_injury-report.py
\`\`\`

Use the sidebar to switch between the Injury Report, Drug Report, and Final Report pages.

## 🤝 Contributing

Feel free to open issues or submit pull requests for bug fixes, new features, or enhancements.
