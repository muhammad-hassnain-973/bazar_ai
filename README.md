# 🇵🇒 BazaarAI — Agentic Sales Data Analyst

**AI-powered business analytics for Pakistani businesses**

Transform your sales data into actionable insights using Groq's LLaMA 3.3 LLM, FastEmbed, and FAISS vector search.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🌟 Features

### 📊 Core Analytics
- **Auto Column Detection** — Automatically identifies date, revenue, product, region, and quantity columns
- **Key Performance Indicators** — Total revenue, average transaction value, MoM growth rates
- **Smart Alerts** — Automatic detection of sales declines, regional underperformance, and opportunities
- **Product Insights** — Top/bottom performers, revenue distribution by product
- **Regional Analytics** — Geographic performance, regional trends over time

### 🤖 AI-Powered Features
- **Executive Summaries** — Groq LLaMA generates SCR (Situation→Complication→Resolution) narratives
- **Natural Language Chat** — Ask questions about your data in English or Roman Urdu
- **Semantic Search** — FAISS-based vector search for data context retrieval
- **Smart Recommendations** — AI-generated growth and optimization recommendations

### 🌐 User Experience
- **Bilingual Support** — English and Roman Urdu (Roman script)
- **Responsive Dashboard** — Full-width tabs for overview, trends, products, regions, summary, chat
- **Dark Green Theme** — Professional, easy-on-the-eyes design
- **Streamlit Cloud Ready** — One-click deployment with secrets management

---

## 🚀 Quick Start

### Local Development

```bash
# Clone repository
git clone https://github.com/yourusername/bazar_ai.git
cd bazar_ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Set API key (get from https://console.groq.com)
export GROQ_API_KEY="your_api_key_here"

# Run app
streamlit run app_new.py
```

Open browser to `http://localhost:8501`

### Streamlit Cloud Deployment

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Select repo and `app_new.py` as main file
4. Add `GROQ_API_KEY` in Secrets section
5. Deploy! 🚀

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## 📋 Input Format

### Required
Your CSV or Excel file should have at least:
- **Revenue Column** — Sales amounts (numeric)

### Recommended
- **Date Column** — Transaction dates (enables trend analysis)
  - Supported formats: `YYYY-MM-DD`, `MM/DD/YYYY`, `DD/MM/YYYY`
- **Product Column** — Product names or SKUs
- **Region Column** — Geographic areas (city, province, country)
- **Quantity Column** — Units sold

### Example Structure

| Date | Product | Region | Revenue | Quantity |
|------|---------|--------|---------|----------|
| 2024-01-15 | Product A | Karachi | 50000 | 100 |
| 2024-01-16 | Product B | Lahore | 75000 | 150 |
| 2024-01-17 | Product A | Islamabad | 45000 | 90 |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                  STREAMLIT APP (app_new.py)          │
│  Dashboard | Trends | Products | Regions | Chat     │
└──────────────────┬──────────────────────────────────┘
                   │
        ┌──────────┴──────────┬───────────┐
        ▼                     ▼           ▼
    ┌────────────┐    ┌──────────────┐ ┌─────────────┐
    │ Ingestion  │    │  Analysis    │ │ Visualization│
    │ (clean)    │    │ (KPIs, trends)    │ (Plotly) │
    └────────────┘    └──────────────┘ └─────────────┘
        │                   │
        └───────────────────┴─────────────┐
                            ▼
                   ┌─────────────────────┐
                   │ Embeddings (FAISS)  │
                   │ (RAG Context)       │
                   └──────────┬──────────┘
                              │
                   ┌──────────┴──────────┐
                   ▼                     ▼
           ┌─────────────────┐  ┌────────────────┐
           │ Groq LLaMA      │  │ Semantic Search│
           │ (AI Analysis)   │  │ (Vector DB)    │
           └─────────────────┘  └────────────────┘
```

### Components

| Module | Purpose |
|--------|---------|
| `app_new.py` | Main Streamlit application |
| `session.py` | Session state management |
| `ingestion.py` | Data loading, cleaning, column auto-detection |
| `analysis.py` | KPI computation, trend analysis |
| `visualization.py` | Plotly chart generation |
| `embeddings.py` | FAISS vector database for RAG |
| `agents.py` | Groq LLaMA API integration |

---

## 🔧 Configuration

### `.streamlit/config.toml`
```toml
[theme]
primaryColor = "#1e7145"          # Dark green
backgroundColor = "#0a0e27"       # Dark background
secondaryBackgroundColor = "#16213e"
textColor = "#e8f0f5"             # Light text

[server]
maxUploadSize = 200               # MB
headless = true
port = 8501
```

### Environment Variables
```bash
GROQ_API_KEY=your_api_key_here
```

---

## 🎯 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Invalid API Key" | Check GROQ_API_KEY in secrets or environment |
| "No date column detected" | Select date column in Column Mapping section |
| Upload fails | Ensure CSV/Excel format, < 50 MB file size |
| Slow analysis | Process fewer rows or columns |

See [DEPLOYMENT.md](DEPLOYMENT.md) for more help.

---

## 📦 Dependencies

- **Streamlit** — Interactive web dashboard
- **Pandas** — Data manipulation
- **Plotly** — Interactive visualizations
- **Groq** — LLaMA API client
- **FastEmbed** — Vector embeddings
- **FAISS** — Vector search database
- **OpenPyXL** — Excel file support

Full list: [requirements.txt](requirements.txt)

---

## 🔐 Security

- ✅ API keys stored in Streamlit secrets (never committed to git)
- ✅ Session data expires after 24 hours
- ✅ No data persistence — uploads discarded after analysis
- ✅ CSRF protection enabled in Streamlit Cloud

---

## 📊 Performance

### Tested With
- ✅ CSV files up to 50 MB
- ✅ 100,000+ transaction records
- ✅ Multiple products and regions
- ✅ 24+ months of historical data

### Optimization Tips
- Pre-aggregate data if possible
- Use recent data (last 12-24 months)
- Remove unnecessary columns
- Streamlit Cloud: 24/7 uptime with auto-scaling

---

## 🌍 Supported Languages

- 🇬🇧 **English** — Full English interface and analysis
- 🇵🇰 **Roman Urdu** — Urdu written in Latin characters (not Arabic script)

---

## 📄 License

MIT License — See LICENSE file

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📧 Support

- 🐛 **Issues**: GitHub Issues
- 💬 **Chat**: Use the in-app Chat feature
- 📖 **Docs**: See DEPLOYMENT.md and code comments

---

## 🙏 Acknowledgments

- **Groq** — LLaMA 3.3 model
- **Streamlit** — Web framework
- **FastEmbed** — Embedding model
- **FAISS** — Vector search library

---

**Built with ❤️ for Pakistani businesses**

**Get started now:** [Streamlit Cloud](https://share.streamlit.io) → Deploy → Connect Secrets → Run! 🚀
